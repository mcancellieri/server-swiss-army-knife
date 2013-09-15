import imp
import os

PluginFolder = "./plugins"
MainModule = "__init__"

def getPlugins():
    plugins = []
    possibleplugins = os.listdir(PluginFolder)
    for i in possibleplugins:
        location = os.path.join(PluginFolder, i)
        if ".py" not in location[-3:]:
            continue
        filename = i[:-3]
        info = imp.find_module(filename, [PluginFolder])
        plugins.append({"name": filename, "info": info})
    return plugins

def loadPlugin(plugin):
    return imp.load_module(MainModule, *plugin["info"])

def searchConverter(self, buttonText):
    print (self.plugins)
    for p in plugin_loader.getPlugins():
        plugin = plugin_loader.loadPlugin(p)
        print (plugin.getName(self))
        if plugin.getName(self) == buttonText:
            return plugin

    
    
    