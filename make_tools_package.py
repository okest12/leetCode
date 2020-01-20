# -*- coding: utf-8 -*-
"""
2016/12/21 first version by @author: sheng.1.ye@nokia.com
    This is the file to make tools package automatically
2017/01/13 update to add new tools, and support selecting multiple files with pattern, by Ye Sheng
2017/02/09 add link.txt and notes.txt for auto_helper tool, by Ye Sheng
2017/02/24 add text_styles.py for edit_dialog highlight text, by Ye Sheng
2017/05/15 add new mmt_check and remove old mmt_check_tool, by Ye Sheng
2017/05/18 update template and example list, by Ye Sheng
2017/06/12 add tools/lib/advanced_listbox.py, by Ye Sheng
2017/06/16 add tools/lib/log_info_dialog.py, by Ye Sheng
2017/07/14 add test_base/version.py, by Ye Sheng
2017/07/14 add tools/log_view/graphic_dialog.py, by Ye Sheng
2017/07/24 add log_view.ico, by Ye Sheng
2017/07/25 add auto_helper.ico, mmt_check.ico, by Ye Sheng
2017/08/23 update to display code number of lines, by Ye Sheng
2017/08/31 add robot_runner, by Ye Sheng
2017/09/19 add function get_version() for tools, and move this file from tools to tools/lib, by Ye Sheng
2017/11/09 add tool log_processor and script_runner, by Ye Sheng
2017/11/23 add tool file_converter, remove tool log_processor, by Ye Sheng
2017/11/06 add tti_tracer_getter, by Ye Sheng
2018/01/12 update to add up_main, and move target files to ./bin, by Ye Sheng
2018/01/16 update to support auto upgrade, by Ye Sheng
2018/01/19 make_package support source_code=False parameter, by Ye Sheng
2018/03/02 improve usability by tool_main_file, tool_depend_file and released_tool_list, by Ye Sheng
2018/03/05 add tk_app_template, by Ye Sheng
2018/03/05 add extract_logs, by Wang Yixiang
2018/03/06 add tool_name.txt in package, by Ye Sheng
2018/03/06 use tool_name as tools subfolder, by Ye Sheng
2018/03/14 avoid updating SHARED_FOLDER if local version is older, by Ye Sheng
2018/09/14 add file auto_helper_item.py, by Ye Sheng
2019/03/29 change for python2 to python3 migration phase I, by Ye Sheng
2019/04/04 change for python2 to python3 migration phase II, by Ye Sheng
2019/04/24 add new tool log_collector, by Ye Sheng
2019/05/15 update xlrd, xlwt file list, by Ye Sheng
2019/07/05 add new tool code_tree, add calculator as demo, by Ye Sheng
"""

import os
import zipfile
import sys
import hashlib
import shutil

_md5 = hashlib.md5 if sys.version_info.major == 2 else lambda x: hashlib.md5(x.encode('utf8'))

suite_root = os.path.abspath(os.path.dirname(__file__)) + '/..' * 6
sys.path.append(suite_root)
root = os.path.abspath(os.path.dirname(__file__) + '/../..')
root in sys.path and sys.path.remove(root)
root in sys.path or sys.path.insert(0, root)

if sys.version_info.major == 2:
    DEFAULT_SHARED_FOLDER = r'\\beeefsn01.china.nsn-net.net\DCM_project\qch2043\up_tools'
else:
    DEFAULT_SHARED_FOLDER = r'\\beeefsn01.china.nsn-net.net\DCM_project\qch2043\up_tools_3'

testsuite_file_list = (
    ('__init__.py', ''),
    ('../../../../tool_name.txt', ''),
    ('../../../../testsuite/__init__.py', ''),
    ('../../../../testsuite/DCM/__init__.py', ''),
    ('../../../../testsuite/DCM/libraries/__init__.py', ''),
)

up_lib_file_list = ('up_lib_file_list_place_holder',)

xlwt_lib_file_list = (
    (('xlwt/', '.*py$', 1), ''),
    ('xlwt/excel-formula.g', ''),
)

xlrd_lib_file_list = (
    (('xlrd/', '.*py$', 1), ''),
)

example_file_list = (
    ('examples/example1_001.py', ''),
    ('examples/example2_001.py', ''),
    ('examples/example3_001.py', ''),
    ('examples/example5_pmi_ri_cqi.py', ''),
    ('examples/example5_pmi_ri_cqi_001.py', ''),
    ('examples/example_set.py', ''),
    ('examples/example_set_1_test_base.py', ''),
    ('examples/example_set_2_test_log.py', ''),
    ('examples/example_set_5_sdata.py', ''),
    ('examples/example_set_6_mmt.py', ''),
    ('examples/example_set_7_common.py', ''),
    ('examples/__init__.py', ''),
)

template_file_list = (
    ('template/__init__.py', ''),
    ('template/FeatureID.py', ''),
    ('template/FeatureID_CaseID.py', ''),
)


tools_lib_file_list = (
    ('tools/__init__.py', ''),
    ('tools/lib/__init__.py', ''),
    (('tools/lib/tkdnd2.8/', '.*.dll', 2), ''),
    (('tools/lib/tkdnd2.8/', '.*.tcl', 2), ''),
    ('tools/lib/TkDND.py', ''),
    ('tools/lib/TwoSideScrolledText.py', ''),
    ('tools/lib/wait_dialog.py', ''),
    ('tools/lib/edit_dialog.py', ''),
    ('tools/lib/text_styles.py', ''),
    ('tools/lib/get_strings_dialog.py', ''),
    ('tools/lib/advanced_listbox.py', ''),
    ('tools/lib/super_extractor.py', ''),
    ('tools/lib/log_info_dialog.py', ''),
    ('tools/lib/select_log_dialog.py', ''),
    ('tools/lib/log_summary_dialog.py', ''),
    ('tools/lib/tk_app.py', ''),
    ('tools/lib/make_tools_package.py', ''),
    ('tools/lib/check.gif', ''),
    ('tools/lib/uncheck.gif', ''),
    (('tools/lib/robot/', '.*py$', 3), ''),
    (('tools/lib/robot/', '.*html$', 3), ''),
    (('tools/lib/robot/', '.*js$', 3), ''),
    (('tools/lib/robot/', '.*css$', 3), ''),
    (('tools/lib/robot_3/', '.*py$', 3), ''),
    (('tools/lib/robot_3/', '.*html$', 3), ''),
    (('tools/lib/robot_3/', '.*js$', 3), ''),
    (('tools/lib/robot_3/', '.*css$', 3), ''),
    (('tools/lib/psutil/', '.*py$', 1), ''),
    (('tools/lib/psutil/', '.*pyd$', 1), ''),
    (('tools/lib/psutil_3/', '.*py$', 1), ''),
    (('tools/lib/psutil_3/', '.*pyd$', 1), ''),
)

# if sys.version_info.major == 2:
#     tools_lib_file_list += (
#         (('tools/lib/psutil/', '.*py$', 1), ''),
#         (('tools/lib/psutil/', '.*pyd$', 1), ''),
#     )
# else:
#     tools_lib_file_list += (
#         (('tools/lib/psutil_3/', '.*py$', 1), ''),
#         (('tools/lib/psutil_3/', '.*pyd$', 1), ''),
#     )

sys_info_file_list = (
    # ('bin/sys_info.bat', '../../../../sys_info.bat'),
    ('test_base/sys_info.ico', ''),
    ('test_base/sys_info.gif', ''),
    ('test_base/sys_info.py', '')
)

log_runner_file_list = (
    # ('bin/log_runner.bat', '../../../../log_runner.bat'),
    ('tools/log_runner/__init__.py', ''),
    ('tools/log_runner/log_runner.py', ''),
    ('tools/log_runner/log_runner.ico', ''),
    ('tools/log_runner/log_runner.gif', ''),
)

log_view_file_list = (
    # ('bin/log_view.bat', '../../../../log_view.bat'),
    ('tools/log_view/__init__.py', ''),
    ('tools/log_view/log_view.py', ''),
    ('tools/log_view/graphic_dialog.py', ''),
    ('tools/log_view/log_view.ico', ''),
    ('tools/log_view/log_view.gif', '')
)

mmt_check_file_list = (
    # ('bin/mmt_check.bat', '../../../../mmt_check.bat'),
    ('tools/mmt_check/__init__.py', ''),
    ('tools/mmt_check/mmt_check.py', ''),
    ('tools/mmt_check/mmt_check.ico', ''),
    ('tools/mmt_check/mmt_check.gif', ''),
    ('tools/mmt_check/Tshark_MMT_sample.txt', ''),
)

auto_helper_file_list = (
    # ('bin/auto_helper.bat', '../../../../auto_helper.bat'),
    ('tools/auto_helper/__init__.py', ''),
    ('tools/auto_helper/auto_helper.py', ''),
    ('tools/auto_helper/auto_helper_item.py', ''),
    ('tools/auto_helper/auto_helper.ini', ''),
    ('tools/auto_helper/log_column_tool.py', ''),
    ('tools/auto_helper/time_tool.py', ''),
    ('tools/auto_helper/sdata_tool.py', ''),
    ('tools/auto_helper/link.txt', ''),
    ('tools/auto_helper/notes.txt', ''),
    ('tools/auto_helper/auto_helper.ico', ''),
    ('tools/auto_helper/auto_helper.gif', ''),
    ('tools/auto_helper/Tshark_MMT_sample.txt', ''),
    (('../../../../testsuite/DCM/user_plane/template/', '.*robot$', 0), ''),
    (('../../../../testsuite/DCM/user_plane/resources/', '.*robot$', 0), ''),
    (('../../../../testsuite/DCM/user_plane/17A/sdata_lrc_edit/', 'SDATA_edit_tool_LTEAPI1220HD_1.0.0.xls', 0), ''),
    (('../../../../resources/DCM/', '.*robot$', 0), ''),
)

robot_runner_file_list = (
    # ('bin/robot_runner.bat', '../../../../robot_runner.bat'),
    ('tools/robot_runner/__init__.py', ''),
    ('tools/robot_runner/robot_runner.py', ''),
    ('tools/robot_runner/robot_runner.ico', ''),
    ('tools/robot_runner/robot_runner.gif', ''),
    ('tools/robot_runner/sample.robot', ''),
)

script_runner_file_list = (
    # ('bin/script_runner.bat', '../../../../script_runner.bat'),
    ('tools/script_runner/__init__.py', ''),
    ('tools/script_runner/script_runner.py', ''),
    ('tools/script_runner/script_runner.ico', ''),
    ('tools/script_runner/script_runner.gif', ''),
    ('tools/script_runner/scripts/__init__.py', ''),
    ('tools/script_runner/scripts/sample.py', ''),
    ('tools/script_runner/scripts/lib/__init__.py', ''),
    ('tools/script_runner/scripts/lib/common.py', ''),
)

file_converter_file_list = (
    # ('bin/file_converter.bat', '../../../../file_converter.bat'),
    ('tools/file_converter/__init__.py', ''),
    ('tools/file_converter/file_converter.py', ''),
    ('tools/file_converter/file_converter.ico', ''),
    ('tools/file_converter/file_converter.gif', ''),
    ('tools/file_converter/tti_tracer_getter.py', ''),
)

up_main_file_list = (
    # ('bin/up_main.bat', '../../../../up_main.bat'),
    ('tools/up_main/__init__.py', ''),
    ('tools/up_main/up_main.py', ''),
    ('tools/up_main/up_tools.py', ''),
    ('tools/up_main/up_main.ico', ''),
)

tk_app_template_file_list = (
    # ('bin/tk_app_template.bat', '../../../../tk_app_template.bat'),
    ('tools/tk_app_template/tk_app_template.py', ''),
    ('tools/tk_app_template/tk_app_template.ico', ''),
    ('tools/tk_app_template/tk_app_template.gif', ''),
)

code_tree_file_list = (
    ('tools/code_tree/code_tree.py', ''),
    ('tools/code_tree/code_tree.ico', ''),
    ('tools/code_tree/code_tree.gif', ''),
)

calculator_file_list = (
    # ('bin/tk_app_template.bat', '../../../../tk_app_template.bat'),
    ('tools/calculator/calculator.py', ''),
    ('tools/calculator/calculator.ico', ''),
    ('tools/calculator/calculator.gif', ''),
)

log_collector_file_list = (
    ('tools/log_collector/log_collector.py', ''),
    ('tools/log_collector/log_collector.ini', ''),
    ('tools/log_collector/log_collector.ico', ''),
    ('tools/log_collector/log_collector.gif', ''),
    (('tools/log_collector/scripts/', '.*\.py', 0), ''),
    (('tools/log_collector/scripts/', '.*\.exe', 0), ''),
)

extract_logs_file_list = (
    # ('bin/extract_logs.bat', '../../../../extract_logs.bat'),
    ('tools/extract_logs/get_logs.py', ''),
    ('tools/extract_logs/extract_logs.py', ''),
    ('tools/extract_logs/extract_logs.ico', ''),
    ('tools/extract_logs/extract_logs.gif', ''),
)

tool_main_file = {
    'auto_helper': (up_lib_file_list, auto_helper_file_list),
    'mmt_check': (up_lib_file_list, mmt_check_file_list),
    'log_view': (up_lib_file_list, log_view_file_list),
    'log_runner': (up_lib_file_list, log_runner_file_list),
    'robot_runner': (robot_runner_file_list,),
    'script_runner': (up_lib_file_list, script_runner_file_list,),
    'file_converter': (up_lib_file_list, file_converter_file_list,),
    'up_main': (up_lib_file_list, up_main_file_list),
    'sys_info': (sys_info_file_list,),
    'extract_logs': (extract_logs_file_list,),
    'log_collector': (log_collector_file_list,),
    'code_tree': (code_tree_file_list,),
    'tk_app_template': (tk_app_template_file_list,),
    'calculator': (calculator_file_list,),

}

tool_depend_file = {
    'auto_helper': (testsuite_file_list, tools_lib_file_list, example_file_list, template_file_list,
                    xlrd_lib_file_list, xlwt_lib_file_list),
    'mmt_check': (testsuite_file_list, tools_lib_file_list,),
    'log_view': (testsuite_file_list, tools_lib_file_list, xlrd_lib_file_list, xlwt_lib_file_list),
    'log_runner': (testsuite_file_list, tools_lib_file_list, xlrd_lib_file_list, xlwt_lib_file_list),
    'robot_runner': (testsuite_file_list, tools_lib_file_list,),
    'script_runner': (testsuite_file_list, tools_lib_file_list,),
    'file_converter': (testsuite_file_list, tools_lib_file_list,),
    'up_main': (testsuite_file_list, tools_lib_file_list),
    'sys_info': (testsuite_file_list, ),
    'extract_logs': (testsuite_file_list, tools_lib_file_list),
    'log_collector': (testsuite_file_list, tools_lib_file_list,),
    'code_tree': (testsuite_file_list, tools_lib_file_list,),
    'tk_app_template': (testsuite_file_list, tools_lib_file_list),
    'calculator': (testsuite_file_list, tools_lib_file_list),
}

released_tool_list = (
    ('up_tools', ('auto_helper', 'mmt_check', 'log_view', 'log_runner', 'robot_runner', 'script_runner',
                  'file_converter', 'up_main')),
    ('log_processor', ('extract_logs', 'file_converter', 'script_runner', 'log_view', 'log_collector',
                       'up_main')),
    ('code_tools', ('auto_helper', 'mmt_check', 'robot_runner', 'code_tree', 'up_main')),
    ('robot_runner', ('robot_runner', 'up_main')),
    ('calculator', ('calculator', 'robot_runner', 'up_main')),
    ('tk_app_template', ('tk_app_template', 'up_main')),
)


def get_version(tool_name=None):
    import re
    import inspect
    base_version, sub_version, sub_version_count = '', '', 0
    up_root = os.path.abspath(os.path.dirname(__file__)) + '/../..'
    version_file_list = []
    if tool_name not in tool_main_file:
        tool_name = 'up_main'
    tool_name = tool_name or os.path.basename(inspect.stack()[1][1]).replace('.pyc', '').replace('.py', '')
    for file_list in tool_main_file[tool_name]:
        if file_list == ('up_lib_file_list_place_holder',):
            from test_base.version import Version
            base_version = Version().get_version()[0] + '.'
        else:
            for item in file_list:
                if type(item[0]) is str:
                    version_file_list.append(item[0])
    for filename in version_file_list:
        if filename.endswith('.py'):
            filename = os.path.join(up_root, filename)
            if not os.path.exists(filename):
                filename += 'c'
            with open(filename, 'rb' if filename.endswith('pyc') else 'r') as rf:
                for line in rf:
                    if filename.endswith('pyc') and sys.version_info.major != 2:
                        line = str(line)
                    m = re.match(r"(..)?(\d\d\d\d)/(\d\d)/(\d\d)", line)
                    if m:
                        version = m.group(2) + m.group(3) + m.group(4)
                        if version > sub_version:
                            sub_version = version
                            sub_version_count = 1
                        elif version == sub_version:
                            sub_version_count += 1
                    m = re.match(r"\s*from tools\.lib\.(\w+)", line)
                    if m and m.group(1) != 'make_tools_package':
                        add_file = os.path.join(up_root, "tools/lib/" + m.group(1) + ".py")
                        if add_file not in version_file_list:
                            version_file_list.append(add_file)
                    if filename.endswith('pyc'):
                        for module in re.findall(r"tools\.lib\.([a-zA-Z_]+)[Rr]", line):
                            if module != 'make_tools_package':
                                add_file = os.path.join(up_root, "tools/lib/" + module + ".py")
                                if add_file not in version_file_list:
                                    version_file_list.append(add_file)
    return base_version + sub_version + ".%d" % sub_version_count


def update_up_lib_file_list(file_list):
    if 'up_lib_file_list_place_holder' in file_list:
        from test_base.version import file_list as up_lib_files
        file_list = [i for i in file_list if i != 'up_lib_file_list_place_holder']
        for filename, _ in up_lib_files + (('test_base/version.py', ''),):
            add_item = filename, ''
            if add_item not in file_list:
                file_list.append(add_item)
    return file_list


def make_package(tool_name=None, source_code=False):
    from test_base.common import find_all_files
    up_root = os.path.abspath(os.path.dirname(__file__)) + '/../..'
    robot_root = os.path.abspath(os.path.dirname(__file__)) + '/..' * 6

    for release_name, tool_list in released_tool_list:
        if tool_name and release_name not in tool_name and release_name != tool_name:
            continue
        with open(os.path.join(suite_root, 'tool_name.txt'), 'w') as wf:
            wf.write(release_name)
        # for tool, file_list, tool_list in up_tool_list:
        all_file_list = []
        for tool in tool_list:
            for file_list in tool_main_file[tool] + tool_depend_file[tool]:
                for item in file_list:
                    if item not in all_file_list:
                        all_file_list.append(item)
        num_of_lines = 0
        num_of_lines_detail = {}
        tool_zip_name = os.path.join(up_root, 'bin/' + release_name + '.zip')
        zip_obj = zipfile.ZipFile(tool_zip_name, 'w', zipfile.ZIP_DEFLATED)
        all_file_list = update_up_lib_file_list(all_file_list)
        for name, target_name in dict(all_file_list).items():
            # up_root = C:\robotlte_trunk\testsuite\DCM\libraries\UP\
            # case1: name = 'tools/auto_helper/auto_helper.py', arcname = ''
            # case2: name = ('../../../../resources/DCM/', '.*robot$', 0), arcname = ''
            # case3: name = 'mmt_check.bat', arcname = '../../../../mmt_check.bat'
            if type(name) is str:
                name = (os.path.join(up_root, name),)
            else:
                name = find_all_files(os.path.join(up_root, name[0]), pattern=name[1], recurse=True, depth=name[2])
            for source_name in name:
                source_name = os.path.abspath(source_name)
                arc_name = target_name or source_name
                arc_name = release_name + '/' + os.path.relpath(os.path.join(up_root, arc_name), robot_root)
                if source_name.endswith('.py'):
                    path = os.path.relpath(os.path.dirname(source_name), robot_root)
                    if 'xlrd' not in path and 'xlwt' not in path:
                        if sys.version_info.major == 2:
                            with open(source_name) as rf:
                                lines = len(rf.readlines())
                        else:
                            with open(source_name, encoding='utf8') as rf:
                                lines = len(rf.readlines())
                        num_of_lines_detail.setdefault(path, 0)
                        num_of_lines_detail[path] += lines
                        num_of_lines += lines
                if (not source_code and source_name.endswith('.py') and 'sample' not in source_name
                        and '\\scripts\\' not in source_name
                        and 'UP\\tools\\' in source_name):
                    import compileall
                    if sys.version_info.major != 2:
                        compileall.compile_file(source_name, force=True, legacy=True)
                    else:
                        compileall.compile_file(source_name, force=True)
                    source_name += 'c'
                    arc_name += 'c'
                if 'psutil' in source_name:
                    print(source_name, arc_name)
                zip_obj.write(source_name, arc_name)

        print("\nTool: %s, code number of lines: %d" % (release_name, num_of_lines))
        for folder, lines in sorted(num_of_lines_detail.items()):
            if lines > 0:
                print("\t%s: %s" % (folder, lines))
        zip_obj.close()
        with open(tool_zip_name + '.ver.txt', 'w') as wf, open(tool_zip_name, 'rb') as rf:
            for t in tool_list:
                wf.write("%s: %s\n" % (t, get_version(t)))
            wf.write("md5: %s\n" % hashlib.md5(rf.read()).hexdigest())
        if os.path.exists(DEFAULT_SHARED_FOLDER):
            bin_path = os.path.join(DEFAULT_SHARED_FOLDER, 'bin')
            if not os.path.exists(bin_path):
                os.mkdir(bin_path, 0o777)
            old_version_file = os.path.join(bin_path, release_name + '.zip.ver.txt')
            if os.path.exists(old_version_file):
                with open(old_version_file) as rf:
                    for line in rf:
                        if ':' in line:
                            tool, old_version = line.rstrip("\n").split(": ")
                            if tool == 'md5':
                                continue
                            new_version = get_version(tool)
                            print(new_version)
                            old_version = [int(i) for i in old_version.split('.')]
                            new_version = [int(i) for i in new_version.split('.')]
                            if sorted([old_version, new_version]) != [old_version, new_version]:
                                info = ("The version of %s on shared_folder is newer!\n%s\n"
                                        "Update anyway?(y/n)"
                                        % (tool, old_version_file))
                                input_check = raw_input(info) if sys.version_info.major == 2 else input(info)
                                if input_check not in ('y', 'Y'):
                                    raise Exception(info)
            for filename in (tool_zip_name, tool_zip_name + '.ver.txt'):
                shutil.copy(filename, os.path.join(DEFAULT_SHARED_FOLDER, 'bin'))
            print("\nCopy %s files to shared_folder done.\n" % release_name)


if __name__ == '__main__':
    # make_package(tool_name='log_processor')
    # make_package(tool_name='calculator')
    make_package()
    for t_name in tool_main_file:
        print("%s version: %s" % (t_name, get_version(t_name)))
