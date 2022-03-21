import logging

# 통상적으로는 어떤 파일에서 이러한 출력되었는지 알고싶어서 주로 __name__ 을 씀
logger = logging.getLogger(__name__) 
f_format = logging.Formatter('%(asctime)s - %(name)s: %(lineno)4d - %(levelname)s - %(message)s')

def main() : 
    # level 은 얼마나 많은 정보를 보여줄지를 나타냅니다.
    logger.info(__name__) 
    # debug 는 어떻게 도는지 모두 다 알려줌
    # 웬만하면 안보는데, 프로그램이 어떻게 도는지 잘 모를때 spamming 을 씁니다.
    logger.debug('debug 구문')
    logger.warning('warining 구문입니다.')
    logger.error('error 구문입니다.')

if __name__ == '__main__' : 
    main() 