def progress_bar():
  for i in range(1, 101):
    print("\r", end="")
    print("Reboot: {}%: ".format(i), "▋" * (i // 1), end="")
    sys.stdout.flush()
    time.sleep(0.7)