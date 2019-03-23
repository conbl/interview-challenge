from collections import defaultdict
from notify import send_email

def users_by_group_id()
  users_dict = defaultdict([])
    for user in json.load(open('json/users.json', 'r'):
      users_dict[user['group_id']].append(user)
  return users_dict

def task_completed(task_id):
    task = next(x for x in json.load(open('json/tasks.json', 'r')) if x['id'] == task_id)
    users_dict = users_by_group_id()

    for user in users_dict[task['group_id']]




