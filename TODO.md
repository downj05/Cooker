- [x] 'Join Server' button *Will start unturned, wait for the menu to load, and join the selected server, does NOT start cooking however*
    - Will need to be able to get StartUnturnedThreads status from main thread


- [ ] Rewrite Cooker to press buttons to start game / join server rather than calling functions itself
    - [x] Fix get window size to work with win32gui rather than pyautogui
    - [ ] Have some way of either setting/adapting to games FOV on startup so images match better
        - Alternatively rather than using image matching if we know the UI scale and resolution we can just use a hash of that as a key in a dictionary of preset screen coordinates
        e.g:

        ```py
        hash = hash_func(screen_x, screen_y, ui_scale)
        
        dict = {
            hash: {
                'menu_button': [20, 139],
            }
        }
        
        ```

- [ ] 'Leave Server' button, 'Join Server' will turn into this when its pressed