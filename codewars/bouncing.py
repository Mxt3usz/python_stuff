def bouncing_ball(h,bounce,window):
    if h > 0 and bounce > 0 and bounce < 1 and window < h:
        acc = h
        count = 1 # count 1 cuz the ball has to be thrown down first
        while True:
            acc = acc * bounce # before checking it has to bounce once
            if acc > window:
                count += 2 # +2 cuz bounce up and down
            if acc < window: # break out if ball cant be seen anymore
                break
        return count
    return -1


print(bouncing_ball(30,0.66,1.5))
print(bouncing_ball(30,0.75,1.5))
