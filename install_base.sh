#!/bin/bash
BASEPATH=$(pwd)

function install_base() {
    #install brew
    /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    #change brew repo USTC（中科大镜像）
    cd "$(brew --repo)"
    git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

    #install wget
    brew install wget
}

function install_zsh() {
    #install zsh
    if [ ! -e '/bin/zsh' ]; then
        wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
    fi
    #power line font
    cp -f zsh/Menlo\ Regular\ for\ Powerline.otf ~/Library/Fonts/
    echo 'You should change your iterm font-style to Menlo Regular for Powerline'
}

function config_zsh() {
    #config
    ln -sf $BASEPATH/zsh/theme/* ~/.oh-my-zsh/themes/
    ln -sf $BASEPATH/zsh/zshrc ~/.zshrc
    source ~/.zshrc
}

function config_iterm() {
    echo "configuring for vim..."
    ln -sf $BASEPATH/iterm/vimrc ~/.vimrc
    echo "installing rz sz for iterm..."
    #rz sz
    brew install lrzsz
    cp -f iterm/iterm2-recv-zmodem.sh /usr/local/bin/
    cp -f iterm/iterm2-send-zmodem.sh /usr/local/bin/
    chmod +x /usr/local/bin/iterm2-recv-zmodem.sh
    chmod +x /usr/local/bin/iterm2-send-zmodem.sh

    echo "*******************************************************************"
    echo "You should go iTerm->Preferences->profile->Advanced->Triggers->Edit"
    echo "and add two triggers:"
    echo "\*\*B0100 RunSilentCoprocess /usr/local/bin/iterm2-send-zmodem.sh"
    echo "\*\*B00000000000000 RunSilentCoprocess /usr/local/bin/iterm2-recv-zmodem.sh"
}





