from django.shortcuts import render
from django.http import HttpResponse
from common.models import Order
# Create your views here.
# def listorders(request):
#     return HttpResponse('下面是系统中所有订单信息。。。')


# 先定义好HTML模板
html_template = '''
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
table {
    border-collapse: collapse;
}
th, td {
    padding: 8px;
    text-align: left;
    border-bottom: 1px solid #ddd;
}
</style>
</head>
    <body>
        <table>
        <tr>
        <th>time</th>
        <th>side</th>
        <th>qty</th>
        <th>symbol</th>
        <th>px</th>
        <th>exchange</th>
        <th>class_type</th>
        <th>description</th>
        <th>tags</th>
        <th>local_time</th>
        <th>source</th>
        <th>orderID</th>
        <th>exchangeOID</th>
        <th>fillID</th>
        <th>strategy</th>
        <th>ilink</th>
        <th>px_multiplier</th>
        <th>multiplier</th>
        <th>TO</th>
        <th>OC</th>
        </tr>

        %s


        </table>
/    </body>
</html>
'''


def listorders(request):
    # 返回一个 QuerySet 对象 ，包含所有的表记录
    qs = Order.objects.values()

    # 检查url中是否有参数phonenumber
    ph = request.GET.get('time', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(time=ph)

    # 生成html模板中要插入的html片段内容
    tableContent = ''
    i = 0
    for order in qs:
        if i == 0:
            i += 1
            continue
        else:
            tableContent += '<tr>'
            for name, value in order.items():
                tableContent += f'<td>{value}</td>'
            tableContent += '</tr>'
    i = 0
    return HttpResponse(html_template % tableContent)