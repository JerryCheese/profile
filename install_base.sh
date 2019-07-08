#!/bin/bash
ROOT=$(pwd)

function init_sys() {
    # install vim
    echo "Installing vim 7.4.2367 ..."
    wget -O- https://github.com/vim/vim/archive/v7.4.2367.tar.gz | tar xvz
    cd vim-7.4.2367/ && ./configure --prefix=$HOME/usr
    make && make install
    cd ../ && rm -rf vim-7.4.2367/

    echo "Configuring vim ..."
    ln -sf $ROOT/files/vimrc ~/.vimrc
    ln -sf $ROOT/files/vim_runtime ~/.vim_runtime
}

function install_zsh() {
    echo "installing zsh..."
    #install zsh
    #brew install zsh
    #sudo yum install -y zsh
    wget -O zsh.tar.xz https://sourceforge.net/projects/zsh/files/latest/download
    xz -d zsh.tar.xz
    mkdir zsh
    tar -xvf zsh.tar -C zsh --strip-components 1
    cd zsh && ./configure --prefix=$HOME/usr
    make && make install
    echo '[ -f $HOME/usr/bin/zsh ] && exec $HOME/usr/bin/zsh -l' >> ~/.bash_profile
    cd ../ && rm -rf zsh

    echo "installing oh-my-zsh..."
    #install oh-my-zsh
    wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh

    echo "setting zsh..."
    #config
    ln -sf $ROOT/zsh/theme/* ~/.oh-my-zsh/themes/
    ln -sf $ROOT/zsh/zshrc ~/.zshrc
    source ~/.zshrc

    #echo "You may need: chsh, and enter '/bin/zsh'"
}
