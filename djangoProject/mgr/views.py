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
        <th>Date</th>
        <th>Open Price</th>
        <th>High Price</th>
        <th>Low Price</th>
        <th>Close Price</th>
        <th>Adj Close Price</th>
        <th>Volume</th>
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
    ph = request.GET.get('date', None)

    # 如果有，添加过滤条件
    if ph:
        qs = qs.filter(create_date=ph)

    # 生成html模板中要插入的html片段内容
    tableContent = ''
    for order in qs:
        tableContent += '<tr>'
        for name, value in order.items():
            tableContent += f'<td>{value}</td>'
        tableContent += '</tr>'

    return HttpResponse(html_template % tableContent)