`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// Company: 
// Engineer: 
// 
// Create Date: 2023/05/10 11:45:17
// Design Name: 
// Module Name: LED
// Project Name: 
// Target Devices: 
// Tool Versions: 
// Description: 
// 
// Dependencies: 
// 
// Revision:
// Revision 0.01 - File Created
// Additional Comments:
// 
//////////////////////////////////////////////////////////////////////////////////


module LED_driver(

    clk, rst, in, led_addr, led_in, ledout, readdata
    );
    input clk;
    input rst;
    input in;
	input[1:0] led_addr;
	input[15:0] led_in;
	output reg[23:0] ledout;
	output reg[15:0] readdata;

    always @(posedge clk, posedge rst) begin
        if (rst) begin 
			ledout <= 24'h0;
			readdata <= 24'h0;
		end
		
	else if (in) begin
		if (led_addr == 2'b00)
		begin
			ledout[15:0] <= led_in[15:0];
			readdata[15:0] <= led_in[15:0];
		end
		else if (led_addr == 2'b10) begin
			ledout[23:16] <= led_in[7:0];
			readdata[15:0] <= {8'h0, led_in[7:0]};
		end
		else begin
			ledout <= led_in;
			readdata[15:0] <= 16'h0;
		end
			
	end
	else begin
		ledout <= ledout;
	end
	end
endmodule
