def add_time(start, duration, day=None):

  new_time = ''

  start = start.split() # list
  start_time = start[0]
  period = start[1] 
  period_shift = str()
  days_past = int()

  start_hour = int(start[0].split(':')[0]) # int 
  start_minute = int(start[0].split(':')[1]) # int

  if period == 'AM':
      period_shift = 'PM'
      total_start_time_minute = start_hour*60 + start_minute # int
  if period == 'PM':
      period_shift = 'AM'
      total_start_time_minute = (12 + start_hour)*60 + start_minute # int
  # whenever a 720 minute cycle is due, the period shifts


  duration = duration.split(':')
  duration_hour = int(duration[0])
  duration_minute = int(duration[1])
  total_duration_minute = duration_hour*60 + duration_minute

  total_time_minute = total_start_time_minute + total_duration_minute 
  shift_count = 0
  total_hour = total_time_minute//60 # for counting days
  days_past = 0 # int
  new_hour = ((start_hour*60 + start_minute) + total_duration_minute)//60 # for counting shifts
  if total_hour >= 24:
      days_past = total_hour//24 # how many days have passed
  if new_hour >= 12:
      shift_count = new_hour//12
      if new_hour%12 == 0:
          new_hour = 12
      else:
          new_hour = new_hour%12   
  new_hour_str = str(new_hour)

  new_minute = 0
  new_minute = total_time_minute - total_hour*60
  new_minute_str = str()
  if new_minute < 10:
      new_minute_str = '0' + str(new_minute)
  else:
      new_minute_str = str(new_minute)

  day_now_index = int() 
  day_later_index = int()
  day_later = str()

  day_dict = {'Monday':1, 'Tuesday':2, 'Wednesday':3, 'Thursday':4, 'Friday': 5, 'Saturday': 6, 'Sunday': 7}
  day_dict_reversed = {1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday', 7: 'Sunday'}


  if day==None:
      if total_time_minute < 24*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift
      elif total_time_minute >= 24*60 and total_time_minute < 48*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period + ' (next day)'
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift + ' (next day)'
      elif total_time_minute >= 48*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period + ' (' + str(days_past) + ' days later)'
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift + ' (' + str(days_past) + ' days later)'    
  else:
      day = day.lower().capitalize()
      day_now_index = day_dict[day] 
      if (day_now_index + days_past)%7 == 0:
          day_later_index = 7  
      else: day_later_index = (day_now_index+days_past)%7
      day_later = day_dict_reversed[day_later_index]
      if total_time_minute < 24*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period + ', ' + day
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift + ', ' + day
      elif total_time_minute >= 24*60 and total_time_minute < 48*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period + ', ' + day_later + ' (next day)'
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift + ', ' + day_later + ' (next day)'
      elif total_time_minute >= 48*60:
          if shift_count%2 == 0:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period + ', ' + day_later + ' (' + str(days_past) + ' days later)'
          else:
              new_time = new_hour_str + ':' + new_minute_str + ' ' + period_shift + ', ' + day_later + ' (' + str(days_past) + ' days later)'    

  return new_time