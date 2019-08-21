class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        fnByContent = collections.defaultdict(list)

        def storeFullFilenamesByContent(cwd, filenames):
            for fn_content in filenames.split():
                fn, content = fn_content[:-1].split('(')
                fnByContent[content].append(cwd+'/'+fn)

        for dir_filenames in paths:
            cwd, filenames = dir_filenames.split(' ', maxsplit=1)
            storeFullFilenamesByContent(cwd, filenames)

        return [val for val in fnByContent.values() if len(val) > 1]
