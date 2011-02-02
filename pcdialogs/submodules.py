from path import path

##def submodules(dir, subdir):
##    packagedir = path(dir).joinpath(subdir)
##    files = packagedir.files()
##    filesfull = [packagedir.joinpath(f) for f in files]
##    modules = []
##    for file, full in zip(files, filesfull):
##        if file!='__init__.py':
##            if full.isdir() or file.ext=='.py':
##                modules.append(file.namebase)
##    return modules
def modules(dir, pattern=None):
    if pattern:
        if not pattern.endswith('.py') :
            pattern = pattern + '.py'
    files = path(dir).files(pattern=pattern)
    return [x.namebase for x in files]
