if status is-interactive
	# Setting colors
	## Prompt
	set -U fish_color_host d93d67
	set -U fish_color_user d93d67
	set -U fish_color_cwd d9613d
	set -U fish_color_status d93d67

	## Input
	set -U fish_color_command 00cf9d
  set -U fish_color_error 86e3c6
  set -U fish_color_autosuggestion 6E988d

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
end