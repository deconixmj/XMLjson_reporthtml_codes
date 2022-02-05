@echo off
::start "E:\pycode\XTS_Sprint_review\XTS_Sprint_review\requirments.txt"
::pip install -r "E:\pycode\XTS_Sprint_review\XTS_Sprint_review\requirments.txt" %*

pip install -r requirments.txt
python gen_html_report_v1.2.py
pause
