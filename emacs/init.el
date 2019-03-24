(defconst user-init-dir
  (cond ((boundp 'user-emacs-directory)
         user-emacs-directory)
        ((boundp 'user-init-directory)
         user-init-directory)
        (t "~/.emacs.d/")))


; Test


(defun load-user-file (file)
  (interactive "f")
  "Load a file in current user's configuration directory"
  (load-file (expand-file-name file user-init-dir)))

(load-user-file "personal.el")
(load-user-file "keyboard.el")
(load-user-file "company-fish.el")

(when (executable-find "fish")
  (add-to-list 'company-backends 'company-fish)
  (add-hook 'shell-mode-hook 'company-mode)
  (add-hook 'eshell-mode-hook 'company-mode))
