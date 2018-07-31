def receive_oreos(patch_push):
	if(patch_push) == True:
		print "Yay, Oreos!"
		return True
	else:
		print "No Oreos for you :("
		return False

patch_push = True
receive_oreos(patch_push)

# Oreos please :D
