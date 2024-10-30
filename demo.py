from nicegui import ui
from nicegui_zeitline import zeitline

ts = zeitline(width=640, height=100)
ts.set_range(start="01 Jan 2017", end="01 Jan 2018")

ts.add_interval("2017-02-01", "2017-04-01", 100)
ts.add_interval("2017-06-01", "2017-08-01", 100)
ts.add_interval("2017-10-01", "2017-12-25", 100)

ts.add_event("31 Jan 2017")
ts.add_event("10 May 2017")
ts.add_event("11 May 2017")
ts.add_event("10 Jun 2017")
ts.add_event("30 Jun 2017")
ts.add_event("24 Dec 2017")

ts.on("zeitlineClick", lambda e: print(e))
ts.on("pivotDrag", lambda e: print(e))

ui.run(port=9001, show=False)
