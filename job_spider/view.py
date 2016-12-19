from django.http import HttpResponse
from spider import job_51job
com = '百度在线网络技术（北京）有限公司'


def hello(request):
    # if request.GET:
    #     data = {}
        # pass
        # data['company'] = request.POST['company']
        # job_51job.spider_job(data['company'])
    job_51job.spider_job(com)
    return HttpResponse("Hello world!")




