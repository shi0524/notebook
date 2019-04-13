# -*- coding: utf-8 –*-

"""
使用python第三方包（apscheduler(3.0.0)）实现定时任务
配置说明：
    任务类型:
        cron: 定时循环任务，类似unix系统的crontab
        interval: 间隔任务， 类型tornado的 percallback
        date: 定点一次性任务， 到指定日期时间运行一次
    cron:
        :param int|str year: 4-digit year
        :param int|str month: month (1-12)
        :param int|str day: day of the (1-31)
        :param int|str week: ISO week (1-53)
        :param int|str day_of_week: number or name of weekday (0-6 or mon,tue,wed,thu,fri,sat,sun)
        :param int|str hour: hour (0-23)
        :param int|str minute: minute (0-59)
        :param int|str second: second (0-59)
        :param datetime|str start_date: earliest possible date/time to trigger on (inclusive)
        :param datetime|str end_date: latest possible date/time to trigger on (inclusive)
        :param datetime.tzinfo|str timezone: time zone to use for the date/time calculations
                                             (defaults to scheduler timezone)
    interval:
        :param int weeks: number of weeks to wait
        :param int days: number of days to wait
        :param int hours: number of hours to wait
        :param int minutes: number of minutes to wait
        :param int seconds: number of seconds to wait
        :param datetime|str start_date: starting point for the interval calculation
        :param datetime|str end_date: latest possible date/time to trigger on
        :param datetime.tzinfo|str timezone: time zone to use for the date/time calculations
    date:
        :param datetime|str run_date: the date/time to run the job at
        :param datetime.tzinfo|str timezone: time zone for ``run_date`` if it doesn't have one already
TIMER_JOBS = (
     任务类型（cron,interval,date）, 任务时间参数(参见上面说明)， 要执行的函数， 是否是全局的
    ('cron', dict(second='5,10,15,20,25,30,55'), timer_arena_award_rank, 1)
)
"""
import time
import gevent.monkey
gevent.monkey.patch_all()
from apscheduler.schedulers.gevent import GeventScheduler
from apscheduler.events import EVENT_JOB_EXECUTED, EVENT_JOB_ERROR

"""
test_func
"""


def test_1():
    print '11111111111111111111111111'
    return 1


def test_2():
    print '22222222222222222222222222'
    return 2


def test_3():
    print '33333333333333333333333333'
    return 3


def test_4():
    print '4444444444444444444444444'
    return 4


def test_5():
    print '5555555555555555555555555'
    return 5


def get_time():

    return ['2019-04-13 15:30:00', '2019-04-13 15:50:00']


# 时区
TIMEZONE = 'Asia/Harbin'

# 任务
TIMER_JOBS = (
    # crotab 结构每10秒执行一次                                                            # 任务
    ('cron', dict(second='*/10'),                                                       test_1),
    # 每周六 15:43 执行
    ('cron', dict(day_of_week='5', hour='15', minute='43'),                             test_2),
    # 每天 15: 43 执行
    ('cron', dict(hour='15', minute='43'),                                              test_3),
    # 每天 2019-4-13 14点-15点 每分钟 执行一次
    ('cron', dict(year='2019', month='4', day='13', hour='19', minute='*'),             test_4),
    # 每天小时的 0分5秒 和 31分5秒 执行一次
    ('cron', dict(hour='0-23', minute='0,31', second='5'),                              test_5),
)

# 任务
DATE_LIST_JOBS = (
    # 返回时间列表的函数（）                       要执行的任务
    (get_time,                                  test_5),
)


class SelfGeventScheduler(GeventScheduler):
    """任务执行类
    重写_main_loop方法, 方便自动更新
    """

    def add_job_to_scheduler(self, trigger_name, trigger_kwargs, job_func):
        job_func_name = '%s:%s' % (job_func.__module__, job_func.__name__)
        job_id = job_func_name
        job = self.add_job(job_func_name, trigger_name,
                           id=job_id, name=job_id,
                           misfire_grace_time=600,
                           replace_existing=True,
                           **trigger_kwargs)
        print job

    def add_time_list_job(self, time_list_func, job_func):
        job_func_name = '%s:%s' % (job_func.__module__, job_func.__name__)
        trigger_name = 'date'
        for index, dt in enumerate(time_list_func()):
            # 过期的timer不再加
            if str(dt) < time.strftime('%F %T'):
                continue
            job_id = '%s:%s' % (job_func_name, index)
            trigger_kwargs = dict(run_date=dt)
            job = self.add_job(job_func_name, trigger_name,
                               id=job_id, name=job_id,
                               misfire_grace_time=600,
                               replace_existing=True,
                               **trigger_kwargs)
            print job

    def reload_all_jobs(self):
        for trigger, trigger_kwargs, func_name in TIMER_JOBS:
            self.add_job_to_scheduler(trigger, trigger_kwargs, func_name)
        for time_list_func, func_name in DATE_LIST_JOBS:
            self.add_time_list_job(time_list_func, func_name)


def my_listener(event):
    now_str = time.strftime('%Y%m%d')
    if event.exception:
        error_msg = '''\n%s\n\nrun at: %s\n\ntraceback info:\n%s
        ''' % (event.job_id,
               event.scheduled_run_time,
               event.traceback)
        subject = ("[RUN_TIMER ERROR] - [%s]") % (now_str)
        """
        报错消息发钉钉群
        try:
            from send_mail import send_dingtalk
            dingtalk = 'https://oapi.dingtalk.com/robot/send?access_token=c5a3886c97dfaf2d9dfa2fd385b8b608f1a9f0fdfe35f6c84ed1014b1be10ed5'
            send_dingtalk(dingtalk, subject, error_msg)
        except:
            pass
        """
    else:
        msg = '%s -- %s\n' % (event.scheduled_run_time, event.job_id)
        print msg


def main():
    scheduler = SelfGeventScheduler(timezone=TIMEZONE)
    scheduler.add_listener(my_listener, EVENT_JOB_EXECUTED | EVENT_JOB_ERROR)
    g = scheduler.start()
    scheduler.reload_all_jobs()

    try:
        g.join()
    except (KeyboardInterrupt, SystemExit):
        pass

if __name__ == "__main__":
    main()

