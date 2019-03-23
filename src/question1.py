import json

LIST_FILTERS = [
  'assigned_user_id',
  'home_id'
]

FILTER_LIST = [
  'home_id',
  'assigned_user_id',
  'schedule_date',
  'task_name',
  'type_priority'
]

def filter_tasks(filters):
  filtered_tasks = []
  all_reservations = json.load(open('json/reservations.json', 'r'))
  all_checkin_dates = { reservation['checkin_date'] for reservation in all_reservations }
  all_checkout_dates = { reservation['checkout_date'] for reservation in all_reservations }
  all_tasks = json.load(open('json/tasks.json', 'r'))

  for task in all_tasks:
    for filter_key in FILTER_LIST:
      if filter_key in filters:
        filter_value = filters[filter_key]

        if filter_key in task:
          if filter_value is None:
            break
          elif filter_key in LIST_FILTERS:
            if task[filter_key] not in filter_value:
              break
          elif task[filter_key] != filter_value:
              break
        elif filter_value is not None:
          break
    else:
      if 'reservation' in filters:
        if 'checkin' in filters['reservation']:
          if task['schedule_date'] not in all_checkin_dates:
            continue

        if 'checkout' in filters['reservation']:
          if task['schedule_date'] not in all_checkout_dates:
            continue

      filtered_tasks.append(task)

  return filtered_tasks