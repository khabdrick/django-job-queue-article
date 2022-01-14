from time import sleep


def hook_funcs(task):
    print("The task result is: ", task.result)


def sleepy_func(sec):
    # This function willl be taken to the job queue
    sleep(sec)
    print ("sleepy function ran")

