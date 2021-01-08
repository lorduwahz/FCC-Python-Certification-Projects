def add_time(start, duration, day=''):
    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    new_day = ''
    dur = duration.split(':')
    dur_h, dur_m = dur[0], dur[1]
    m_sta = start.split(' ')
    _sta, am_pm = m_sta[0], m_sta[1]
    sta = _sta.split(':')
    sta_h, sta_m = sta[0], sta[1]
    am_pm_holder, n_am_pm, no_days = ['AM', 'PM'], '', 0
    step_h, step_m = (int(dur_h) % 24) + int(sta_h), int(dur_m) + int(sta_m)
    new_time_h, new_time_m = 0, 0

    if int(dur_h) % 24 == 0:
        no_days = int(dur_h) // 24
        n_am_pm = m_sta[1]

    elif step_h > 11 and am_pm == 'PM':
        no_days = 1 + (int(dur_h) // 24)
        n_am_pm = 'AM'

    elif step_h > 11 and am_pm == 'AM':
        no_days = int(dur_h) // 24
        n_am_pm = 'PM'

    elif step_h < 11:
        no_days = int(dur_h) // 24
        n_am_pm = m_sta[1]

    if int(dur_h) % 12 == 0:
        new_time_h = int(sta_h)

    elif ((int(dur_h) % 12) + int(sta_h)) > 12:
        new_time_h = ((int(dur_h) % 12) + int(sta_h)) - 12

    else:
        new_time_h = int(dur_h) % 12 + int(sta_h)

    if (int(dur_m) + int(sta_m)) > 59:
        new_time_h = new_time_h + 1
        new_time_m = (int(dur_m) + int(sta_m)) - 60

        if new_time_h > 11 and am_pm == 'PM':
            no_days = no_days + 1
            n_am_pm = 'AM'

        elif new_time_h > 11 and am_pm == 'AM':
            n_am_pm = 'PM'

    else:
        new_time_m = int(dur_m) + int(sta_m)

    for i in days:
        if day == i and no_days % 7 == 0:
            new_day = days[days.index(day.capitalize())]

        elif day == i and (no_days % 7) <= 7:
            new_day = days[((days.index(day.capitalize()) + (no_days % 7)) - 7)]

    if day == '' and no_days == 0:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm}'
    elif day == '' and no_days == 1:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm} (next day)'
    elif day == '' and no_days > 1:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm} ({no_days} days later)'
    else:
      new_day = days[((days.index(day.capitalize()) + (no_days % 7)) - 7)]
      if no_days == 0:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm}, {new_day}'
      elif no_days == 1:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm}, {new_day} (next day)'
      else:
        return f'{str(new_time_h)}:{str(new_time_m).zfill(2)} {n_am_pm}, {new_day} ({no_days} days later)'
