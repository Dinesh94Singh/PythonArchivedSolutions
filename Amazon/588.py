"""
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is
a directory path, return the list of file and directory names in this directory. Your output (file and directory
names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the
middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create
that file containing given content. If the file already exists, you need to append given content to original content.
This function has void return type.

readContentFromFile: Given a file path, return its content in string format.



Example:

Input:
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Explanation:
filesystem


Note:

You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that
the path is just "/". You can assume that all operations will be passed valid parameters and users will not attempt
to retrieve file content or list a directory or file that does not exist. You can assume that all directory names and
file names only contain lower-case letters, and same names won't exist in the same directory. """

"""
public class FileSystem {
    class File {
        boolean isfile = false;
        HashMap < String, File > files = new HashMap < > ();
        String content = "";
    }
    File root;
    public FileSystem() {
        root = new File();
    }

    public List < String > ls(String path) {
           d = path.split('/')
        temp = self.root

        res = []
        for idx, each in enumerate(d):
            if temp.files.get(each, None):
                temp = temp.files.get(each, None)

            if idx == len(d) - 1:
                res.append(temp.files)
        return res
        
        File t = root;
        List < String > files = new ArrayList < > ();
        if (!path.equals("/")) {
            String[] d = path.split("/");
            for (int i = 1; i < d.length; i++) {
                t = t.files.get(d[i]);
            }
            if (t.isfile) {
                files.add(d[d.length - 1]);
                return files;
            }
        }
        List < String > res_files = new ArrayList < > (t.files.keySet());
        Collections.sort(res_files);
        return res_files;
    }

    public void addContentToFile(String filePath, String content) {
        File t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) {
            t = t.files.get(d[i]);
        }
        if (!t.files.containsKey(d[d.length - 1]))
            t.files.put(d[d.length - 1], new File());
        t = t.files.get(d[d.length - 1]);
        t.isfile = true;
        t.content = t.content + content;
    }

    public String readContentFromFile(String filePath) {
        File t = root;
        String[] d = filePath.split("/");
        for (int i = 1; i < d.length - 1; i++) {
            t = t.files.get(d[i]);
        }
        return t.files.get(d[d.length - 1]).content;
    }
}
"""


class Structure:
    def __init__(self, is_file=False, content=None):
        self.is_file = is_file
        self.content = content
        self.files = {}


class FileSystem:
    def __init__(self):
        self.root = Structure()

    def ls(self, path: str):
        d = path.split('/')
        temp = self.root

        res = []
        for idx, each in enumerate(d):
            if temp.files.get(each, None):
                temp = temp.files.get(each, None)

            if idx == len(d) - 1\
                    `and len(temp.files) > 0:
                res.append(temp.files.keys)
        return res.sort()

    def mkdir(self, path: str) -> None:
        d = path.split("/")
        temp = self.root
        for idx, each in enumerate(d):
            if idx == 0:
                continue
            if not temp.files.get(each, None):
                temp.files[d[idx]] = Structure()
                temp = temp.files[d[idx]]
        return None

    def addContentToFile(self, filePath: str, content: str) -> None:
        # t.isfile = True
        # t.content = t.content + content;

        d = filePath.split('/')
        temp = self.root
        for idx, each_dir in enumerate(d):
            if temp.files.get(each_dir, None):
                temp = temp.files[each_dir]

            # TODO: Create a directory, if the path is not found
            if idx == len(d) - 2:
                if not temp.files.get(d[idx + 1], None):
                    # if file not found, create the file
                    temp.files[d[idx + 1]] = Structure(True, content)
                    return
                else:
                    file = temp.files[d[idx + 1]]
                    file.content = file.content + content
                    temp.files[d[idx + 1]] = file
                    return
        return

    def readContentFromFile(self, filePath: str) -> str:
        t = self.root
        d = filePath.split('/')

        for idx, each_dir in enumerate(d):
            if idx == 0:
                continue
            if t:
                t = t.files.get(each_dir, None)

        return t.content if t.is_file else None


root = FileSystem()
root.mkdir('/a/b/c')
print(root.ls('/a'))
print(root.ls('/a/b'))
print(root.readContentFromFile('/a/b/c'))
root.addContentToFile('/a/b/c/d', 'hello')
print(root.readContentFromFile('/a/b/c/d'))
root.addContentToFile('/a/b/c/d', ' Dinesh')
print(root.readContentFromFile('/a/b/c/d'))
# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)
