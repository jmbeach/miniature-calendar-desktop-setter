/usr/bin/osascript<<END
tell application "Finder" 
	set desktop picture to POSIX file "$(pwd)/todays-img.jpg" 
end tell
END
