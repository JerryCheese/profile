#!/bin/bash
ROOT=$(pwd)

function init_sys() {
    echo "installing brew..."
    #install brew

    if [ ! -e '/usr/local/bin/brew' ]; then
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    echo "change brew repo to USTC.."
    #change brew repo USTC（中科大镜像）
    cd "$(brew --repo)"
    git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

    echo "installing dependencies softwares..."
    #install wget lrzsz
    brew install wget lrzsz

    #link hosts
    echo "linking hosts..."
    sudo ln -sf $ROOT/mac/hosts /etc/hosts

    #vim
    echo "configuring for vim..."
    ln -sf $ROOT/iterm/vimrc ~/.vimrc
}

function install_zsh() {
    echo "installing zsh..."
    #install zsh
    brew install zsh

    echo "installing oh-my-zsh..."
    #install oh-my-zsh
    if [ ! -e '/bin/zsh' ]; then
        wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sh
    fi

    echo "coping Power Line Font..."
    #power line font
    cp -f zsh/Menlo\ Regular\ for\ Powerline.otf ~/Library/Fonts/
    echo 'You should change your iterm font-style to Menlo Regular for Powerline'

    echo "setting zsh..."
    #config
    ln -sf $ROOT/zsh/theme/* ~/.oh-my-zsh/themes/
    ln -sf $ROOT/zsh/zshrc ~/.zshrc
    source ~/.zshrc
}

function config_iterm() {
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

function config_vscode() {
    ln -nsf $ROOT/vscode ~/Library/Application\ Support/Code/User
}



