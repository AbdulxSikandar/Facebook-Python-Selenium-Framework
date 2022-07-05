

# class HtmlReport(self.driver):
#     def __init__(self):
#         self.driver = driver
#
#     def htmlreport(self):
#         pytest_html = item.config.pluginmanager.getplugin('html')
#         outcome = yield
#         report = outcome.get_result()
#         extra = getattr(report, 'extra', [])
#
#         if report.when == 'call' or report.when == "setup":
#             xfail = hasattr(report, 'wasxfail')
#             if (report.skipped and xfail) or (report.failed and not xfail):
#                 file_name = report.nodeid.replace("::", "_") + ".png"
#                 _capture_screenshot(file_name)
#                 if file_name:
#                     html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
#                            'onclick="window.open(this.src)" align="right"/></div>' % file_name
#                     extra.append(pytest_html.extras.html(html))
#             report.extra = extra
