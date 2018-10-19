#!/bin/bash
ROOT=$(pwd)

function init_sys() {
    #install brew
    if [ ! -e '/usr/local/bin/brew' ]; then
        echo "installing brew..."
        /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
    fi

    #change brew repo USTC（中科大镜像）
    echo "change brew repo to USTC.."
    cd "$(brew --repo)"
    git remote set-url origin https://mirrors.ustc.edu.cn/brew.git
    cd "$(brew --repo)/Library/Taps/homebrew/homebrew-core"
    git remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git

    #install wget lrzsz
    echo "installing dependencies softwares..."
    brew install wget lrzsz

    #link hosts
    echo "linking hosts..."
    sudo chown root $ROOT/mac/hosts
    sudo chgrp whell $ROOT/mac/hosts
    sudo chmod 644 $ROOT/mac/hosts
    sudo ln -df $ROOT/mac/hosts /etc/hosts

    #vim
    echo "configuring for vim..."
    ln -sf $ROOT/iterm/vimrc ~/.vimrc

    #delte to trash, support only one file/dir
    echo "linking deltotrash..."
    ln -sf $ROOT/lib/deltotrash.sh /usr/local/bin/deltotrash.sh
    chmod +x /usr/local/bin/deltotrash.sh
}

function install_zsh() {
    echo "installing zsh..."
    #install zsh
    #brew install zsh
    sudo yum install -y zsh

    echo "installing oh-my-zsh..."
    #install oh-my-zsh
    sudo wget https://github.com/robbyrussell/oh-my-zsh/raw/master/tools/install.sh -O - | sudo sh

    #echo "coping Power Line Font..."
    #power line font
    #cp -f zsh/Menlo\ Regular\ for\ Powerline.otf ~/Library/Fonts/
    #cp -f zsh/Monaco\ for\ Powerline.otf ~/Library/Fonts/

    #echo 'You should change your iterm font-style to Menlo Regular for Powerline'

    echo "setting zsh..."
    #config
    ln -sf $ROOT/zsh/theme/* ~/.oh-my-zsh/themes/
    ln -sf $ROOT/zsh/zshrc ~/.zshrc
    source ~/.zshrc

    echo "You may need: chsh, and enter '/bin/zsh'"
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



