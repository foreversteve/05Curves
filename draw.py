from display import *
from matrix import *


def add_circle( points, cx, cy, cz, r, step ):
	x = cx + r
	y = cy

	t = 0
	while t < 1:
		theta = t * 2 * math.pi
		x = cx + r * math.cos(theta)
		y = cy + r * math.sin(theta)
		add_point(points,x,y)
		t+=step

def add_curve( points, x0, y0, x1, y1, x2, y2, x3, y3, step, curve_type ):
	x_list = [[x0,x1,x2,x3]]
	y_list = [[y0,y1,y2,y3]]

	print(x_list[0])

	if curve_type == "hermite":
		hermite = make_hermite()
		
		matrix_mult(hermite,x_list)
		matrix_mult(hermite,y_list)

	if curve_type == "bezier":
		bezier = make_bezier()

		matrix_mult(bezier,x_list)
		matrix_mult(bezier,y_list)

	a,b,c,d = [x_list[0][0],x_list[0][1],x_list[0][2],x_list[0][3]]

	e,f,g,h = [y_list[0][0],y_list[0][1],y_list[0][2],y_list[0][3]]

	t = 0
	while t < 1:
		x = a * math.pow(t,3)+b * math.pow(t,2)+c*t+d
		y = e * math.pow(t,3)+f * math.pow(t,2)+g*t+h

		add_point(points,x,y)
		t += step


def draw_lines( matrix, screen, color ):
	if len(matrix) < 2:
		print('Need at least 2 points to draw')
		return

	point = 0
	while point < len(matrix) - 1:
		draw_line( int(matrix[point][0]),
				   int(matrix[point][1]),
				   int(matrix[point+1][0]),
				   int(matrix[point+1][1]),
				   screen, color)    
		point+= 2
		
def add_edge( matrix, x0, y0, z0, x1, y1, z1 ):
	add_point(matrix, x0, y0, z0)
	add_point(matrix, x1, y1, z1)
	
def add_point( matrix, x, y, z=0 ):
	matrix.append( [x, y, z, 1] )
	



def draw_line( x0, y0, x1, y1, screen, color ):

	#swap points if going right -> left
	if x0 > x1:
		xt = x0
		yt = y0
		x0 = x1
		y0 = y1
		x1 = xt
		y1 = yt

	x = x0
	y = y0
	A = 2 * (y1 - y0)
	B = -2 * (x1 - x0)

	#octants 1 and 8
	if ( abs(x1-x0) >= abs(y1 - y0) ):

		#octant 1
		if A > 0:            
			d = A + B/2

			while x < x1:
				plot(screen, color, x, y)
				if d > 0:
					y+= 1
					d+= B
				x+= 1
				d+= A
			#end octant 1 while
			plot(screen, color, x1, y1)
		#end octant 1

		#octant 8
		else:
			d = A - B/2

			while x < x1:
				plot(screen, color, x, y)
				if d < 0:
					y-= 1
					d-= B
				x+= 1
				d+= A
			#end octant 8 while
			plot(screen, color, x1, y1)
		#end octant 8
	#end octants 1 and 8

	#octants 2 and 7
	else:
		#octant 2
		if A > 0:
			d = A/2 + B

			while y < y1:
				plot(screen, color, x, y)
				if d < 0:
					x+= 1
					d+= A
				y+= 1
				d+= B
			#end octant 2 while
			plot(screen, color, x1, y1)
		#end octant 2

		#octant 7
		else:
			d = A/2 - B;

			while y > y1:
				plot(screen, color, x, y)
				if d > 0:
					x+= 1
					d+= A
				y-= 1
				d-= B
			#end octant 7 while
			plot(screen, color, x1, y1)
		#end octant 7
	#end octants 2 and 7
#end draw_line
