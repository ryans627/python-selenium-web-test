import pytest
import os

# 项目主程序入口
# 默认运行所有测试用例
pytest.main(['-vs', '--clean-alluredir', '--alluredir', './allure_result'])

# 清理旧的测试报告，将allure的测试结果分析生成HTML报告
os.system('allure generate ./allure_result -o ./report --clean')