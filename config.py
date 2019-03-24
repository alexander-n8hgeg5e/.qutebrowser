config.load_autoconfig()



from qutebrowser.utils import objreg
from qutebrowser.api import cmdutils
from qutebrowser.completion.models import urlmodel

def is_most_right_tab():
  if get_last_tab_id() == get_current_tab_id():
      return True
  else:
    return False

def get_current_tab():
  return (objreg._get_registry("tab",tab='current'))['tab']

def get_current_tab_id():
  return (objreg._get_registry("tab",tab='current'))['tab'].tab_id

def get_tabs():
  return (objreg.get("tab-registry",scope='window',window='current'))

def number_of_tabs():
  return len(get_tabs())

def get_last_tab_id():
  """it is asumed that the dict index matches the tab id.
  """
  return list(get_tabs())[-1]

def tabnew():
  #print(dir(get_current_tab()))
  get_cmd_dispatcher().openurl(tab=True)

def get_cmd_dispatcher():
  return objreg.get('command-dispatcher',scope='window',window='current')

def get_quitter():
  return objreg.get('quitter')

def tabnext():
  get_cmd_dispatcher().tab_next()


@cmdutils.register(name='condtabnext')
def conditional_tabnext():
    """switch to the next tab or if it is the one at the most right position, open a new one.
    """
    #print(get_current_tab_id())
    #print(get_current_tab())
    #print(number_of_tabs())
    if is_most_right_tab():
        tabnew()
    else:
        tabnext()

def is_the_only_tab():
  if number_of_tabs() == 1:
    return True
  else:
    return False

@cmdutils.register(name='tabquitclose')
def tabquitclose():
    """close tab. if last tab quit.
    """
    #print(get_current_tab_id())
    #print(get_current_tab())
    #print(number_of_tabs())
    #print(dir(get_quitter()))
    if is_the_only_tab():
        pass
        #print(dir(get_cmd_dispatcher()))
        get_quitter().quit()
    else:
        get_cmd_dispatcher().tab_close()


@cmdutils.register(name='e',maxsplit=0)
@cmdutils.argument('url', completion=urlmodel.url)
def _openurl(url):
    """
    opens url
    """
    get_cmd_dispatcher().openurl(url)

# tabs:
config.bind('<Ctrl-Left>', 'tab-prev')
config.bind('<Ctrl-Right>', 'condtabnext')
config.bind('<Ctrl-s>', 'tab-prev')
config.bind('<Ctrl-f>', 'condtabnext')

# caret mode:
#       movement:
config.bind( '<Up>',    'move-to-prev-line' , 'caret'   )
config.bind( '<Down>',  'move-to-next-line' , 'caret' )
config.bind( '<Left>',  'move-to-prev-char', 'caret' )
config.bind( '<Right>', 'move-to-next-char', 'caret' )
config.bind( 'e',  'run-with-count 4 move-to-prev-line',  'caret')
config.bind( 'd',  'run-with-count 4 move-to-next-line',  'caret' )
config.bind( 's',  'move-to-prev-word',   'caret' )
config.bind( 'f',  'move-to-next-word',   'caret' )
#       scrolling: 
#                  slow:
# <slow scroll placeholder>
#          "
#          "
#          "
#                  fast:
config.bind( 'i',  'scroll-px 0 -80',     'caret')
config.bind( 'k',  'scroll-px 0  80',     'caret')
config.bind( 'j',  'scroll-px -30 0',     'caret')
config.bind( 'l',  'scroll-px  30 0',     'caret')

#normal mode:
#        movement(movement not avail. so scroll)
config.bind( '<Up>',    'scroll up'   )
config.bind( '<Down>',  'scroll down' )
config.bind( '<Left>',  'move-to-prev-char' )
config.bind( '<Right>', 'move-to-next-char')
config.bind( 'e',  'scroll-px   0 -80' )
config.bind( 'd',  'scroll-px   0  80'  )
config.bind( 's',  'scroll-px -30   0' )
config.bind( 'f',  'scroll-px  30   0')
#        scrolling:
#                  slow:
# <slow scroll placeholder>
#          "
#          "
#          "
#                  fast:
config.bind( 'i',  'scroll-px 0 -80')
config.bind( 'k',  'scroll-px 0  80')
config.bind( 'j',  'scroll-px -30 0')
config.bind( 'l',  'scroll-px  30 0')

#other stuff:
config.bind( '<Space>',  'hint')
config.bind('<Ctrl-q>', 'tabquitclose')
config.bind('<Ctrl-q>', 'tabquitclose','command')
config.bind('<Ctrl-Down>', 'set-cmd-text :')
config.bind('<Ctrl-d>', 'set-cmd-text :')
config.bind('<Ctrl-Up>', 'leave-mode', 'command')
config.bind('<Ctrl-e>', 'leave-mode', 'command')
config.bind('<PgUp>', 'completion-item-focus prev', 'command')
config.bind('<PgDown>', 'completion-item-focus next', 'command')
config.bind('<Ctrl-PgUp>', 'completion-item-focus prev-category', 'command')
config.bind('<Ctrl-PgDown>', 'completion-item-focus next-category', 'command')
config.bind('p', 'insert-text {clipboard}')
config.bind('p', 'insert-text {clipboard}')
config.bind('<Del>', 'tab-close')
config.bind('a', 'enter-mode insert')
config.unbind('ad')
config.bind( '<,>',  'back'           )
config.bind( '<.>',  'forward'        )

c.colors.tabs.bar.bg='#000000'
c.colors.tabs.even.bg='#000000'
c.colors.tabs.even.fg='#ffffff'
#colors.tabs.indicator.error='#000000'
#colors.tabs.indicator.start='#000000'
#colors.tabs.indicator.stop='#000000'
#colors.tabs.indicator.system='#000000'
c.colors.tabs.odd.bg='#000000'
c.colors.tabs.odd.fg='#ffffff'
c.colors.tabs.selected.even.bg='#55aaff'
c.colors.tabs.selected.odd.bg='#55aaff'
c.colors.tabs.selected.even.fg='#ffff00'
c.colors.tabs.selected.odd.fg='#ffff00'
