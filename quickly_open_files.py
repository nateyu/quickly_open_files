import sublime, sublime_plugin, os

class QuicklyOpenFilesCommand(sublime_plugin.WindowCommand):
  def __init__(self, window):
    sublime_plugin.WindowCommand.__init__(self, window)
    self.opened_files = []
    self.enabled      = True

  def selected(self, index):
    if index >= 0:
      target_file = self.opened_files[index][1]
      self.window.open_file(target_file)

    self.enabled = True

  def run(self, file_name=None):
    files = []
    for i in self.window.views():
      files.append([os.path.basename(i.file_name()), i.file_name()])

    self.opened_files = files

    if self.enabled:
      self.enabled = False
      self.window.show_quick_panel(self.opened_files, self.selected)

