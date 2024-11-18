# Weathersched

Weather app that uses `huey` for scheduling.

## Notes

### huey app

The code for my `huey` app is in [`src/weathersched/huey_app/`](./src/weathersched/huey_app/). The `huey` storage/backend is configured in [`src/weathersched/huey_app/config.py`](./src/weathersched/huey_app/config.py), and tasks are defined in [`src/weathersched/huey_app/tasks.py`](./src/weathersched/huey_app/tasks.py).

A simple SQLite backend configuration in `huey_app/config.py` might look like:

```python
from huey import SqliteHuey

# Initialize Huey with SQLite backend
huey = SqliteHuey(filename='huey.db')
```

The `huey_app/tasks.py` file imports the `huey` app from `huey_app/config`, and adds tasks using decorator functions. An example `huey_app/tasks.py` file might look like:

```python
from huey import crontab, CancelExecution
from .config import huey

@huey.task()
def add(a, b):
    return a + b

## Run task every minute, retry 3 times delaying 10 seconds each time, expire task after 45 seconds
@huey.periodic_task(crontab(minute="*/1"), retries=3, retry_delay=10, expires=45)
def say_hello_each_minute():
    print("Hello, from Huey! I do this every minute...")
    return
```

### Running a consumer

`huey` requires a consumer to be running for tasks to be callable. When you run a consumer, `huey` discovers all tasks and starts a worker that waits for tasks to be called.

Start a consumer by activating your `.venv` and running a command like the following:

```shell
## Run the consumer by calling the huey storage backend in huey_app.config
huey_consumer.py <app_name>.huey_app.config.huey
```

You can add `--logfile=path/to/huey.log` to enable file logging, and `--verbose` for verbose logging. Note that when you enable logging to a file, console output is no longer logged.

### Calling tasks

Once you [have a consumer running](#running-a-consumer), you can import tasks from your `huey` app and call them with delays, timeouts, & more.

For example, running the `add()` function with `blocking=True` which tells `huey` to wait for the execution to finish because this is not an async function:

```python
from <app_name>.huey_app.tasks import add

result = add(1,2)
print(f"1 + 2 = {result.get(blocking=True)}")
```
