from api.threadpools._base import (FIRST_COMPLETED,
                                      FIRST_EXCEPTION,
                                      ALL_COMPLETED,
                                      CancelledError,
                                      TimeoutError,
                                      Future,
                                      Executor,
                                      wait,
                                      as_completed)
from api.threadpools.thread import ThreadPoolExecutor


def goThreadPoolExecutor(func, params,max_workers=3):
     with  ThreadPoolExecutor(max_workers=max_workers) as executor:
        all_task = [executor.submit(func, params=param) for param in params]
        response = list()
        for future in as_completed(all_task):
            response.extend(future.result())
        return response