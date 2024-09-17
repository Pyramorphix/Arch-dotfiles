if status is-interactive
  # Useful bindings 
  alias vim nvim
  alias wgup "sudo wg-quick up"
  alias wgdown "sudo wg-quick down"


  function prompt_login --description 'display user name for the prompt'
    if not set -q __fish_machine
        set -g __fish_machine
        set -l debian_chroot $debian_chroot

    if test -r /etc/debian_chroot
            set debian_chroot (cat /etc/debian_chroot)
        end

    if set -q debian_chroot[1]
            and test -n "$debian_chroot"
            set -g __fish_machine "(chroot:$debian_chroot)"
        end
    end

  # Prepend the chroot environment if present
  if set -q __fish_machine[1]
        echo -n -s (set_color yellow) "$__fish_machine" (set_color normal) ' '
    end

  # If we're running via SSH, change the host color.
  set -l color_host $fish_color_host
    if set -q SSH_TTY; and set -q fish_color_host_remote
        set color_host $fish_color_host_remote
    end

  echo -n -s (set_color $fish_color_user) "$USER" (set_color $fish_color_cwd) " 󰆧 " (set_color $color_host) (prompt_hostname) (set_color normal)
  end


  function fish_greeting
    echo -n "Welcome back, Pyramorphix! " | lolcat -F .15
    switch (random 1 6)
      case 1
        echo "And remember: $(tput bold)never stop grinding"
      case 2
        echo "Don't forget to drink some "(set_color 2acaea)"water"
      case 3
        echo "This message will self-destruct"
      case 4
        echo "Segmentation fault (core dumped)" 
      case 5
        echo ""
      case 6
        echo -n "Welcome back, Pyramorphix! " | lolcat -F .15
        echo "(Multicast x2)"
    end
  end

  # Convenient clear
  alias cl clear

  # Convenient cd + clear
  alias cdl "cd && clear"

  # Convenient clear + neofetch
  alias cln "clear && neofetch"
  
  # I LIKE TRAINS!!!!
  function trainarmy
    clear
    for i in (seq 1 10)
      sl -2ec
    end
    clear
  end

  # Enabling fzf:
  eval (fzf --fish)
  fzf_key_bindings
  
  # Binding bat (better cat):
  export BAT_THEME=catppuccin_mocha
  alias cat bat

  # Binding eza (better ls):
  alias ls "eza --icons=always --oneline"
  
  # Configuring thefuck:
  thefuck --alias | source
  alias f fuck
  alias бля fuck

  # Binding zoxide (better cd):
  eval "$(zoxide init fish)"
  alias cd z

  # Setting up fzf:
  export FZF_CTRL_T_OPTS="--preview 'bat -n --color=always --line-range :500 {}'"
  export FZF_ALT_C_OPTS="--preview 'eza --tree --color=always {} | head -200'"

end

