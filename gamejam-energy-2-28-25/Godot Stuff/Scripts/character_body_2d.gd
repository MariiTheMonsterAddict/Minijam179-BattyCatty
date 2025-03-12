extends CharacterBody2D

const min_charge = 0
const max_charge = 100
const SPEED = 700.0
const JUMP_VELOCITY = -1000.0
var charge = 0 


func _physics_process(delta: float) -> void:
	if true:
		print (charge , "<- Charge Debug")
		if charge > max_charge :
			
			pass
		elif charge != max_charge :
			charge += 80 * delta 
			charge = roundf(charge) 
		
	
	# Add the gravity.
	if not is_on_floor():
		velocity += get_gravity() * delta

	# Handle jump.
	if Input.is_action_just_pressed("ui_accept") and is_on_floor():
		velocity.y = JUMP_VELOCITY
		print("charge rest <-Debug")
		charge = 0 

	# Get the input direction and handle the movement/deceleration.
	# As good practice, you should replace UI actions with custom gameplay actions.
	var direction := Input.get_axis("ui_left", "ui_right")
	print (velocity.x)
	if velocity.x == 0 :
			print ("not moving at all")
	

	if direction:
		velocity.x = direction * SPEED
		if velocity.x < 0.1 : #if moving left 
			print ("moving left")
		
		if velocity.x > -0.1 : #if moving right 
			print ("moving right")		
		if velocity.x == 0: #flips baty depending on the direction she is facing
			return
		$Sprite2D.flip_h = true if velocity.x < 0 else false
		
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)
	
	move_and_slide()
