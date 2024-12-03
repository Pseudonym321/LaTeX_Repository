def Riemann_sum(initial_bound:float, terminal_bound:float, number_of_denominations:int):
    """
    Purpose:
        Given two bounds and a number of denominations, returns the width of the individual denominations.
    Parameters:
        float - initial_bound: 
        float - terminal_bound:
        int - number_of_denominations:
    Return:
        float - denomination_width:
        list[float] - left_Riemann_inputs
    """
    denomination_width = (terminal_bound - initial_bound)/number_of_denominations # - float
    left_Riemann_inputs = [(initial_bound + denomination_number * denomination_width) for denomination_number in range(number_of_denominations)]
    return denomination_width, left_Riemann_inputs





