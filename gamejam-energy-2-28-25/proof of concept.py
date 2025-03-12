import amdgpu_stats
import os
import sys
import GPUtil
import pygame


def GetGpuBrand():
    try :
        deviceID = GPUtil.getFirstAvailable()
        
        GpuBrand = "Nvidia"
       
    except RuntimeError :
        GpuBrand = "AMD"
        
    return(GpuBrand)
    
#Gets power from nvidia/amd gpus puts them into variables ### Fix later
def GetGpuPower(GpuBrand): 
    if GpuBrand == "Nvidia":
        print("stinky nvidia card")
        gpu_power_usage = 69
    elif GpuBrand == "AMD":
        amdgpu_power = amdgpu_stats.utils.get_power_stats()
    
        gpu_power_limit = amdgpu_power.get('limit')
        gpu_power_current = amdgpu_power.get('usage')
        gpu_power_usage = amdgpu_power.get('usage_pct')
        gpu_power_usage = round(gpu_power_usage / 100, 2)
        if gpu_power_usage >= 1: 
            gpu_power_usage = 1
    else :
        print("Your Gpu doesnt like my game... Sorry!!")
    return(gpu_power_usage)
    
    
def GameLoop(brand):
    pygame.init()
    TickMult = 2 
    Myscreen = pygame.display.set_mode((800, 800))
    clock = pygame.time.Clock()
    dt = 0
    button_pressTime = 0
    while True:
        gpu_power_usage = GetGpuPower(brand)
        powerscale = gpu_power_usage * TickMult
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                TickMult += .2
                button_pressTime = pygame.time.get_ticks()
                Myscreen.fill((255, 255, 255))
        
        MyCurrent_Time = pygame.time.get_ticks()
        if MyCurrent_Time - button_pressTime > 2000:
            Myscreen.fill((0, 0, 0))
        pygame.display.flip()
        dt = (clock.tick(60 * powerscale)) /1000
        
        print(dt, "<- Delta Time")
        print(powerscale,"<- Power Scale")
        print(gpu_power_usage, "<- Power Usage")
        print(TickMult, "<- Tick Mult")
def main():
    brand = GetGpuBrand()
    GameLoop(brand)
    
main()