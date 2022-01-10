def main():
    generator = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
    return sum(generator)

if __name__ == '__main__':
    print(main())