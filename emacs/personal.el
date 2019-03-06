(require 'package)

(setq backup-directory-alias `(("." . "~/emacs-saves")))
(setq backup-by-copying t)
(setq delete-old-versions t
      kept-new-versions 20
      kept-old-versions 10
      version-control t)

(setq package-archives '(("gnu" . "https://elpa.gnu.org/packages/")
			 ("melpa" . "https://melpa.org/packages/")))
