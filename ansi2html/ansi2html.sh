#!/bin/sh

# Convert ANSI (terminal) colours and attributes to HTML

# Modified from the original Author:
#    http://www.pixelbeat.org/docs/terminal_colours/

p='\x1b\['        #shortcut to match escape codes
P="\(^[^°]*\)¡$p" #expression to match prepended codes below

# Handle various xterm control sequences.
# See /usr/share/doc/xterm-*/ctlseqs.txt
sed "
s#\x1b[^\x1b]*\x1b\\\##g  # strip anything between \e and ST
s#\x1b][0-9]*;[^\a]*\a##g # strip any OSC (xterm title etc.)

#handle carriage returns
s#^.*\r\{1,\}\([^$]\)#\1#
s#\r\$## # strip trailing \r

# strip other non SGR escape sequences
s#[\x07]##g
s#\x1b[]>=\][0-9;]*##g
s#\x1bP+.\{5\}##g
s#\x1b(B##g
s#${p}[0-9;?]*[^0-9;?m]##g

#remove backspace chars and what they're backspacing over
:rm_bs
s#[^\x08]\x08##g; t rm_bs
" |

# Normalize the input before transformation
sed "
# escape HTML
s#\&#\&amp;#g; s#>#\&gt;#g; s#<#\&lt;#g; s#\"#\&quot;#g

# normalize SGR codes a little

# split 256 colors out and mark so that they're not
# recognised by the following 'split combined' line
:e
s#${p}\([0-9;]\{1,\}\);\([34]8;5;[0-9]\{1,3\}\)m#${p}\1m${p}¬\2m#g; t e
s#${p}\([34]8;5;[0-9]\{1,3\}\)m#${p}¬\1m#g;

:c
s#${p}\([0-9]\{1,\}\);\([0-9;]\{1,\}\)m#${p}\1m${p}\2m#g; t c   # split combined
s#${p}0\([0-7]\)#${p}\1#g                                 #strip leading 0
s#${p}1m\(\(${p}[4579]m\)*\)#\1${p}1m#g                   #bold last (with clr)
s#${p}m#${p}0m#g                                          #add leading 0 to norm

# undo any 256 color marking
s#${p}¬\([34]8;5;[0-9]\{1,3\}\)m#${p}\1m#g;

# map 16 color codes to color + bold
s#${p}9\([0-7]\)m#${p}3\1m${p}1m#g;
s#${p}10\([0-7]\)m#${p}4\1m${p}1m#g;

# change 'reset' code to a single char, and prepend a single char to
# other codes so that we can easily do negative matching, as sed
# does not support look behind expressions etc.
s#°#\&deg;#g; s#${p}0m#°#g
s#¡#\&iexcl;#g; s#${p}[0-9;]*m#¡&#g
" |

# Convert SGR sequences to HTML
sed "
:ansi_to_span # replace ANSI codes with CSS classes
t ansi_to_span # hack so t commands below only apply to preceeding s cmd

/^[^¡]*°/ { b span_end } # replace 'reset code' if no preceeding code

# common combinations to minimise html (optional)
s#${P}3\([0-7]\)m¡${p}4\([0-7]\)m#\1<span class=\"f\2 b\3\">#;t span_count
s#${P}4\([0-7]\)m¡${p}3\([0-7]\)m#\1<span class=\"f\3 b\2\">#;t span_count

s#${P}1m#\1<span class=\"bold\">#;                            t span_count
s#${P}4m#\1<span class=\"underline\">#;                       t span_count
s#${P}5m#\1<span class=\"blink\">#;                           t span_count
s#${P}7m#\1<span class=\"reverse\">#;                         t span_count
s#${P}9m#\1<span class=\"line-through\">#;                    t span_count
s#${P}3\([0-9]\)m#\1<span class=\"f\2\">#;                    t span_count
s#${P}4\([0-9]\)m#\1<span class=\"b\2\">#;                    t span_count

s#${P}38;5;\([0-9]\{1,3\}\)m#\1<span class=\"ef\2\">#;        t span_count
s#${P}48;5;\([0-9]\{1,3\}\)m#\1<span class=\"eb\2\">#;        t span_count

s#${P}[0-9;]*m#\1#g; t ansi_to_span # strip unhandled codes

b # next line of input

# add a corresponding span end flag
:span_count
x; s/^/s/; x
b ansi_to_span

# replace 'reset code' with correct number of </span> tags
:span_end
x
/^s/ {
  s/^.//
  x
  s#°#</span>°#
  b span_end
}
x
s#°##
b ansi_to_span
"
