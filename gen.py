for i in range(2,18):
    g = '''		gridboxtype = {
			name = "fallingblocks_row_%d"
			position = { x = 32 y = %d }
			size = { width = 320 height = 32 }
			slotsize = { width = 32 height = 32 }
			max_slots_horizontal = 10
			max_slots_vertical = 0
		}''' % (i, (i-2)*32)
    sg = '''			fallingblocks_row_%d = {
				array = fallingblocks_row_%d
				entry_container = fallingblocks_block_entry
			}''' % (i,i)
    print(g)