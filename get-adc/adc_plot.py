#!/bin/env python3

import matplotlib.pyplot as plt

def plot_voltage_vs_time(time, voltage, max_voltage):
    plt.figure(figsize=(10, 6))
    plt.xlabel("Время, с")
    plt.ylabel("Напряжение, В")
    plt.grid(True)
    plt.plot(time, voltage)
    plt.title("График зависимости напряжения на входе АЦП от времени")
    plt.legend()
    plt.show()

def plot_sampling_period_hist(time):
    values = [time[i] - time[i - 1] for i in range(1, len(time))]
    print(values)
    plt.figure(figsize=(10, 6))
    plt.hist(values)
    plt.xlabel("Период измерения, с")
    plt.ylabel("Количество измерений")
    plt.xlim(0, 0.06)
    plt.grid(True)
    plt.title("Распределение периодов дискретизации измерений по времени на одно измерение")
    plt.legend()
    plt.show()
    
