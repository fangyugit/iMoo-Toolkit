def progress_bartest():
  os.system('cls')
  namef=input('firstname:')
  namel=input('lastname:')
  tim=input('time:')
  inf=input('fill:')
  info=input('f/s:')
  info=int(info)
  tim=int(tim)
  namef = namef+"  {}%: "
  namel = " "+namel
  for i in range(1, 101):
      print("\r", end="")
      print(namef.format(i), inf * (i // info), end=namel)
      sys.stdout.flush()
      time.sleep(tim)