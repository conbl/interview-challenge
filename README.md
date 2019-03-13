# Breezeway Interview Questions 

## Requirements

- Python >=3.5

## Installation and Running Tests

    1. Clone repository to local directory
    2. Run tests using pytest 
    
### Additional Packages

If any additional packages are needed, please add them to `requirements.txt`.

## Data Source

All data for the questions can be found in the `/json` directory. They are files that include valid json to be used as sample data for your methods. 

## Questions

### Question 1: Task Filtering 

Implement the `def filter_tasks(filters)` method in `src/question1.py`, This method should be able to filter on the following data points: home_id, assigned_user_id, type_priority, schedule_date, task_name, when reservation check in or check out date matches the schedule date of a task, and if the task is part of a workflow.

Filter Input:

```json

{
    "home_id": [123, 21],
    "assigned_user_id": [75, 12],
    "schedule_date": "2019-07-23",
    "task_name": "Mid-week Check-up",
    "reservation": ["checkin", "checkout"],
    "type_priority": "Normal"
}

```

Any omitted filters are ignored, any filters that pass null mean that that filter_tasks should return results where the value is not present.

For example:

```json
    "home_id": [123],
    "schedule_date": None,
```

This would return all tasks that are scheduled at home_id 123, and where the schedule_date is not set for the task. It will not be present in the data set.



#### Method Call Example

```python

filter_tasks({
    "home_id": [123, 21],
    "assigned_user_id": [75, 12],
    "schedule_date": "2019-07-23",
    "task_name": "Mid-week Check-up",
    "reservation": ["checkin", "checkout"] 
})

```

#### Reservation Filtering

Filtering on reservations works slightly different than the other examples. When the `reservation` key is passed to the filter method, it uses the data found in `json/reservation.json` as the values for the filter.

If `{"reservation": ["checkin"]` is passed, your code should filter down to any tasks where the `schedule_date` of the task matches the `checkin_date` of *any* reservation in the data set. 

### Question 2: Task Completion and Notification 

Implement the `def task_completed(task_id)` method found in `src/question2.py`. This method should take in a task_id and call the `send_email()` method found in `src/notify/__init__.py` for each user who should recieve the notifcation.

#### Notification Rules

When a task is completed, we should notify all supervisors whose department matches the completed task. 

When a task is completed, and the task is part of a workflow, the user assigned to the next task should be notified. The workflow data can be found in `/json/workflows.json`. The task_id key holds the tasks, in order of completion. 

For example, when `task_id = 10`  is completed. We will send the `worker-task-ready` notifcation to the assigned user of `task_id = 18`
