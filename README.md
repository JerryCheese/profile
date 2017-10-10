一些个人配置
### 初始化系统
* 安装brew、wget、lrzsz
* brew使用[中科大镜像源](https://lug.ustc.edu.cn/wiki/mirrors/help/brew.git)
* 将`mac/hosts` 软链到 `/etc/hosts`，使用时需要手动解密hosts.enc文件
* 将`iterm/vimrc` 软链到 `~/.vimrc`

### 安装zsh、oh-my-zsh以及配置
* 将`zsh/zshrc` 软链到 `~/.zsh_rc`
* 安装了`Menlo Regular for Powerline`字体，需要手设iterm字体
* 将`zsh/themes/*` 软链到 `~/.oh-my-zsh/themes`，zsh自带的theme能用，同时加了自己的theme进去

### iterm
* 安装了lzsz触发器，但是需要手动设置iterm的trigger

### ssr
* 使用`tools/enc.sh`进行加密解密，同时ignore了解密后的文件
* 需要自己更新-设置pac list

### vscode
* 将`vscode`目录 软链到 `~/Library/Application Support/Code/User` 以用作vscode的配置
* 同时ignore了缓存目录`vscode/workspaceStorage`及其子目录/文件

