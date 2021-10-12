import stock_data.funds as funds
import analysis_tools.correlation_matrix as cm

def main():

    assets = funds.sp500_stocks()[110:150]

    correlation_matrix = cm.correlation_matrix_generator(assets, period='1y', interval='1d', visual=True, img_name='Image dump/TEST')
    print(correlation_matrix)

if __name__ == '__main__':

    main()

