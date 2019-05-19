# Mac 환경설정

**참고**

[본격 macOS에 개발 환경 구축하기](https://subicura.com/2017/11/22/mac-os-development-environment-setup.html#그래서)

> neovim 플러그인은 설치하면 느려짐

[macOS Setup Guide](https://sourabhbajaj.com/mac-setup)

------

- Xcode

```
$ xcode-select --install
$ sudo installer -pkg /Library/Developer/CommandLineTools/Packages/macOS_SDK_headers_for_macOS_10.14.pkg -target /
```

- homebrew

```
$ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
$ echo 'export PATH="/usr/local/bin:$PATH"' >> ~/.zshrc
$ brew tap caskroom/cask
```

- iterm2

```
# iterm2
$ brew cask install iterm2
$ brew tap caskroom/fonts && brew cask install font-source-code-pro
```

- zsh

```
$ brew install zsh zsh-completions
```

- ohmyzsh

```
$ sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
$ source ~/.zshrc
```

- ohmyzsh plugin -1

```
$ git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
# vi ~/.zshrc 에 plugins 다음과 같이 수정
plugins=( [plugins...] zsh-syntax-highlighting)
$ source ~/.zshrc
```

- ohmyzsh plugin -2

```
$ git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
# vi ~/.zshrc 에 plugins 다음과 같이 수정
plugins=( [plugins...] zsh-autosuggestions)
$ source ~/.zshrc
```

- git

```
$ brew install git git-lfs
$ git config --global user.name "Your Name Here"
$ git config --global user.email "your_email@youremail.com"
$ git config --global credential.helper osxkeychain
$ git config --global color.ui true
$ git config --global core.precomposeunicode true
$ git config --global core.quotepath false
```

- gitignore_global

```
$ vi ~/.gitignore_global # 내용채운후
$ git config --global core.excludesfile ~/.gitignore_global
```

- pyenv

```
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
$ echo 'eval "$(pyenv init -)"' >> ~/.zshrc
$ source ~/.zshrc
$ pyenv install --list
$ pyenv install 3.6.7
$ pyenv global 3.6.7
$ pyenv rehash
$ pyenv versions
```

- pyenv-virtualenv

```
$ git clone https://github.com/pyenv/pyenv-virtualenv.git $(pyenv root)/plugins/pyenv-virtualenv
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
$ source ~/.zshrc
```