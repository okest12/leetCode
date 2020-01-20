# -*- coding: utf-8 -*-
"""
2018/01/10 first version by @author: sheng.1.ye@nokia.com
    This is the file to make tools exe package automatically
2018/01/16 update to support auto upgrade, by Ye Sheng
2018/03/05 add tk_app_template, by Ye Sheng
2018/03/05 add extract_logs, by Wang Yixiang
2018/03/06 include pythonw.exe and python.exe into package, by Ye Sheng
2018/03/06 use tool_name as tools subfolder, use up_main.exe as application name, by Ye Sheng
2018/03/15 fix issue of packing additional files into target exe file, by Ye Sheng
2019/03/29 change for python2 to python3 migration phase I, by Ye Sheng
2019/04/24 add debug_flag, by Ye Sheng
2019/07/05 add calculator as demo, by Ye Sheng
"""

import os
import zipfile
import re
import sys
import shutil
from make_tools_package import DEFAULT_SHARED_FOLDER

root = os.path.abspath(os.path.dirname(__file__) + '/../..')
root in sys.path and sys.path.remove(root)
root in sys.path or sys.path.insert(0, root)
from test_base.common import find_all_files

# input_file_pattern = r'C:\robotlte_trunk\testsuite\DCM\libraries\UP\{name}.zip'
# output_file_pattern = r'C:\robotlte_trunk\testsuite\DCM\libraries\UP\{name}_exe.zip'

PYTHON_PATH = r'c:\python27' if sys.version_info.major == 2 else r'c:\python36'


make_exe_cmd = (PYTHON_PATH + r'\scripts\pyinstaller ..\up_main\up_tools.py {console} -y '
                r'-n {app_name} '
                r'-i {lib_path}\..\up_main\up_main.ico '
                r'--distpath {folder}\dist '
                r'--workpath {folder}\build '
                r'--specpath {folder}\build')

tools_list = [{'name': 'up_tools',
               'input':
               ((r'.\bin\up_tools.zip', '..'),
                (PYTHON_PATH + r'\lib\site-packages\matplotlib_one_folder.zip', '')),
               'output': r'.\bin\up_tools_exe.zip'},

              {'name': 'robot_runner',
               'input': ((r'.\bin\robot_runner.zip', '..'),),
               'output': r'.\bin\robot_runner_exe.zip'},

              {'name': 'log_processor',
               'input': ((r'.\bin\log_processor.zip', '..'),
                         (PYTHON_PATH + r'\lib\site-packages\matplotlib_one_folder.zip', '')),
               'output': r'.\bin\log_processor_exe.zip'},

              {'name': 'code_tools',
               'input': ((r'.\bin\code_tools.zip', '..'),),
               'output': r'.\bin\code_tools_exe.zip'},

              {'name': 'tk_app_template',
               'input': ((r'.\bin\tk_app_template.zip', '..'),),
               'output': r'.\bin\tk_app_template_exe.zip'},

              {'name': 'calculator',
               'input': ((r'.\bin\calculator.zip', '..'),),
               'output': r'.\bin\calculator_exe.zip'},

              ]


def unzip_file(zipfilename, unziptodir, strip_level=0):
    if not os.path.exists(unziptodir):
        os.mkdir(unziptodir, 0o777)
    zfobj = zipfile.ZipFile(zipfilename)
    for name in zfobj.namelist():
        name = name.replace('\\', '/')
        new_name = name
        for i in range(strip_level):
            new_name = re.sub('^.*?/', '', new_name)
        if new_name.endswith('/'):
            os.mkdir(os.path.join(unziptodir, new_name))
        elif new_name:
            ext_filename = os.path.join(unziptodir, new_name)
            ext_dir = os.path.dirname(ext_filename)
            if not os.path.exists(ext_dir):
                os.makedirs(ext_dir, 0o777)
            outfile = open(ext_filename, 'wb')
            outfile.write(zfobj.read(name))
            outfile.close()


def make_exe(tools=None, debug_flag=False):

    if type(tools) is not tuple:
        tools = (tools,)
    tmp_folder = os.environ["TMP"]
    for tool in tools_list:
        tool_name = tool['name']
        if not tools or tool_name in tools:
            working_folder = os.path.join(tmp_folder, 'up_tools')
            tools_folder = os.path.join(tmp_folder, 'up_tools/dist/%s' % tool_name)
            print("Use pyinstaller to generate up_main.exe in folder: %s" % tools_folder)
            console = '-c' if debug_flag else '-w'
            os.system(make_exe_cmd.format(folder=working_folder, app_name=tool_name, console=console,
                                          lib_path=os.path.dirname(__file__)))
            for input_file, sub_folder in tool.get('input', []):
                input_file = os.path.join(root, input_file)
                folder = os.path.join(tools_folder, sub_folder)
                print("Unzip %s to folder: %s" % (input_file, folder))
                unzip_file(input_file, folder)
            # shutil.copy(PYTHON_PATH + r"\pythonw.exe", tools_folder)
            # shutil.copy(PYTHON_PATH + r"\python.exe", tools_folder)
            shutil.move(os.path.join(tools_folder, "%s.exe" % tool_name),
                        os.path.join(tools_folder, "up_main.exe"))
            output_file = os.path.join(root, tool['output'])
            print("Create output file %s from %s" % (output_file, tools_folder))
            target_zip_obj = zipfile.ZipFile(output_file, 'w', zipfile.ZIP_DEFLATED)
            for file_name in find_all_files(tools_folder, depth=-1):
                target_zip_obj.write(file_name, arcname=os.path.relpath(file_name, start=os.path.dirname(tools_folder)))
            target_zip_obj.close()
            if os.path.exists(DEFAULT_SHARED_FOLDER):
                shutil.copy(output_file, os.path.join(DEFAULT_SHARED_FOLDER, 'bin'))

if __name__ == '__main__':
    make_exe('up_tools')
    # make_exe('robot_runner')
    # make_exe('tk_app_template')
    make_exe('log_processor', debug_flag=False)
    make_exe('code_tools', debug_flag=False)
    # make_exe('calculator', debug_flag=False)
    make_exe(debug_flag=False)
    print("out folder: %s" % os.path.join(DEFAULT_SHARED_FOLDER, 'bin'))
