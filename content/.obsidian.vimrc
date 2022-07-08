# My .vimrc for Obsidian. See: 'Obsidian Vimrc Support Plugin'.
# Have j and k navigate visual lines rather than logical ones.
nmap j gj
nmap k gk

# H and L for jumping to the beginning/end of line
# nmap H ^
# nmap L $

# Yank to system clipboard
set clipboard=unnamed

# Go back and forward with Ctrl+O and Ctrl+I
# (make sure to remove default Obsidian shortcuts for these to work)
exmap back obcommand app:go-back
nmap <C-o> :back
exmap forward obcommand app:go-forward
nmap <C-i> :forward

exmap wiki surround [[ ]]
map [[ :wiki

