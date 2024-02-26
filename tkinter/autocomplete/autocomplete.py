# QUICKSTART

import tkinter as tk
from autoMain import AutocompleteEntry

root = tk.Tk()

frame = tk.Frame(root)
frame.pack()

entry = AutocompleteEntry(frame)
# You can pass additional parameters to further customize the window;
# all parameters that you can pass to tk.Frame, are valid here too.


ENTRIES = (
    "Foo",
    "Bar",
    "Who",
    "Far"
)

# entry.build(ENTRIES)
# You can pass additional parameters to "build"
"""
max_entries (integer):
The maximum number of entries to display at once. This value directly corresponds to the listbox widget's height attribute. Defaults to 5.

case_sensitive (boolean):
If True, only autocomplete entries that enforce the same capitalization as the current entry will be displayed.
If False, all autocomplete entries that match with the current entry will be displayed.
Defaults to False.

no_results_message (string or None):
The message to display if no suggestions could be found for the current entry.
This argument may include a formatting identifier ({}) which, at runtime, gets formatted as the current entry. If None is specified, the listbox will instead be hidden until the next <KeyRelease> event.
"""

entry.build(
    entries=ENTRIES,
    no_results_message="< Ekkert finnst fyrir '{}' >"
) # Note that tis is formatted at runtime

entry.pack()

# Now, each time a user presses a key while the entry widget has focus, a list of suggetions will display below it.

# ADDITIONAL OPTIONS
"""
By default, the tk.Listbox widget has a width of 25 pixels and a height of 5 (items). The tk.Entry widget also has a default width of 25 pixels. These settings can be modified through the following class attributes:

AutocompleteEntry.LISTBOX_HEIGHT: The height to specify when creating the tk.Listbox widget. There's no need to modify this, since the maximum number of entries to be displayed can be passed as an argument to build.

AutocompleteEntry.LISTBOX_WIDTH: The width to specify when creating the tk.Listbox widget. Any positive integer is valid.

AutocompleteEntry.ENTRY_WIDTH: The width to specify when creating the tk.Entry widget. Any positive integer is valid.

NOTE: You almost always want to keep the 1:1 LISTBOX_WIDTH:ENTRY_WIDTH ratio.
You can retrieve the current entry by accessing the instance's text attribute (which is a tk.StringVar instance):

text = entry.text.get()
To further customize the entry widget, you may set its font options, for example:

entry.entry["font"] = (<FONT NAME>, <FONT SIZE>, <FONT WEIGHT>)
Or to change the background color for the listbox widget:

entry.listbox["background"] = "#cfeff9"
# Light blue
"""

root.mainloop()