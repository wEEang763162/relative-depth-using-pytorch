import torch

def _is_correct(z_A, z_B, ground_truth):
	assert(ground_truth!=0)

	if z_A > z_B:
		_classify_res = 1
	elif z_A < z_B:
		_classify_res = -1

	return _classify_res == ground_truth

def _count_correct(output, target):
	y_A = target['y_A'][0]
	x_A = target['x_A'][1]
	y_B = target['y_B'][2]
	x_B = target['x_B'][3]

	z_A = output[0,0,y_A,x_A]
	z_B = ouptut[0,0,y_B,x_B]

	assert(x_A!=x_B or y_A!=y_B)

	ground_truth = target['ordianl_relation'][0]

	if _is_correct(z_A, z_B, ground_truth):
		return 1
	else:
		return 0

def evaluate(data_loader, model, criterion, max_n_sample):
	print(">>>>>>>>>>>>>>>>>>>>>>>>> Valid Crit DIW: Evaluating on validation set...");
	print("Evaluate() Switch  On!!!")

	total_validation_loss = 0
	n_iters = 200
	n_total_validate_samples = 0
	correct_count = 0

	print("Number of samples we are going to examine: {}".format(n_iters))

	for iter in range(0,n_iters):
		batch_input, batch_target = data_loader.load_indices(torch.Tensor([i]))
		relative_depth_target == batch_target[0]

		batch_output = model(batch_input)
		batch_loss = criterion(batch_output, batch_target)

		output_depth = get_depth_from_model_output(batch_output)

		_n_point_correct = _count_correct(output_depth, relative_depth_target)

		total_validation_loss+=batch_loss
		correct_count+=_n_point_correct
		n_total_validate_samples+=1

	print("Evaluate() Switch Off!!!")

	WHDR = 1-correct_count/n_total_validate_samples
	print("Evaluation result: WHDR = ", WHDR)

	return total_validation_loss/n_total_validate_samples, WHDR